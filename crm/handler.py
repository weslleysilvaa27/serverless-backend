import json
import boto3
import logging
import requests
from os import environ

DEBUG = environ.get('debug', 'F')
ERP_BUCKET_NAME = environ["erp_bucket_name"]

LOG = logging.getLogger('crm')
LOG.setLevel(logging.DEBUG if DEBUG.upper() == "T" else boto3.logging.WARNING)

session = boto3.Session(region_name=environ.get("region", "us-east-1"))
S3_CLIENT = session.client("s3")


def main(event, context):

    for row in event["Records"]:
        err, data = get_object(row["s3"]["object"]["key"])
        if err:
            LOG.exception(err)
            
        payload = {
            "Pedidos": {
                "value": data
            }
        }
        resp = requests.post("http://httpbin.org/post", json=payload)
        LOG.info(resp.text)


def get_object(key: str) -> tuple[str, dict]:
    kwargs = {
        "Bucket": ERP_BUCKET_NAME,
        "Key": key
    }
    try:
        resp = S3_CLIENT.get_object(**kwargs)
        cont = resp['Body'].read().decode('utf-8')

        obj = json.loads(cont)
        
        return "", obj
        
    except Exception as e:
        return e, {}