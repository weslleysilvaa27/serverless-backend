import json
import boto3
import logging
from os import environ
from multiprocessing import Process, Pipe
from botocore.exceptions import ClientError

PATH_FILE = "./erp_data.json"
DEBUG = environ.get('debug', 'F')
ERP_BUCKET_NAME = environ["erp_bucket_name"]

LOG = logging.getLogger('erp')
LOG.setLevel(logging.DEBUG if DEBUG.upper() == "T" else boto3.logging.WARNING)

session = boto3.Session(region_name=environ.get("region", "us-east-1"))
S3_CLIENT = session.client("s3")


def main(event, context):
    err, data = read_file()
    if err:
        return response(500, err)

    processes = []
    parent_connections = []

    for item in data:
        parent_conn, child_conn = Pipe()
        parent_connections.append(parent_conn)

        process = Process(target=put_object, kwargs={"data": item, "connection": child_conn})
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    for row in parent_connections:
        err = (row.recv())[0]
        if isinstance(err, ClientError):
            LOG.error(f"main(1): {err.response['Error']['Code']} - {err.response['Error']['Message']}")
            return response(500, f"Erro ao salvar os items no bucket")

    return response(200, "Dados processados com sucesso")


def put_object(data: dict, connection: list):
    payload = {
        "Bucket": ERP_BUCKET_NAME,
        "Key": f"{data['id']}.json",
        "ContentType": "application/json",
        "Body": json.dumps(data)
    }
    try:
        _ = S3_CLIENT.put_object(**payload)
        connection.send([None])
    except ClientError as e:
        connection.send([e])

    connection.close()


def read_file() -> tuple[str, list[dict]]:
    try:
        with open(PATH_FILE, 'r', encoding='utf-8') as file:
            data = json.loads(file.read())
            return "", data

    except FileNotFoundError as e:
        LOG.error(f"Arquivo não localizado para leitura: {e}")
        return "Arquivo não localizado para leitura", []

    except Exception as e:
        LOG.error(f"Erro interno no servidor: {e}")
        return "Erro interno no servidor", []


def response(status_code: int, body: str) -> dict:
    return {
        "statusCode": status_code, 
        "body": json.dumps(body, ensure_ascii=False)
    }
