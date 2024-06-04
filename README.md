# Serverless Back-end

Back-end construindo utilizando Serverless Framework.

## Pré-requisitos

### Instalar AWS CLI Linux - [awscli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
```
Arquitetura x86
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update

Arquitetura Arm
curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update
```

### Instalar Node.js - [node](https://nodejs.org/en/download/package-manager)
```
sudo apt install nodejs
```


### Instalar Serverless Framework - [serverlessframework](https://www.serverless.com/framework/docs/getting-started)
```
npm i serverless -g
```

### Instalar Plug-in Package Python - [pluginpython](https://www.serverless.com/plugins/serverless-package-python-functions)
```
npm install --save serverless-package-python-functions
```

## Configurações

### Ter uma conta na AWS para criação de um Usuário IAM
![Screenshot from 2024-05-31 23-19-42](https://github.com/weslleysilvaa27/serverless-backend/assets/171731302/cedda78e-16d6-4e98-84a7-707b04e66d5a)

![Screenshot from 2024-05-31 23-22-08](https://github.com/weslleysilvaa27/serverless-backend/assets/171731302/a20465af-86a7-4b0a-b81f-d719a4c1a469)

![Screenshot from 2024-05-31 23-23-39](https://github.com/weslleysilvaa27/serverless-backend/assets/171731302/bc9320f1-799d-497f-956c-0a3c9570363a)



### Selecionar a Aba Credenciais de Segurança e criar a Chaves de acesso para obter o AccessKey e SecretKey
![Screenshot from 2024-05-31 23-24-28](https://github.com/weslleysilvaa27/serverless-backend/assets/171731302/9e28dbcb-6b30-4d2b-ab20-8b318ff8719c)



###

### Configurar as credenciais da etapa anterior
```
aws configure
```

## Deploy

### Deployar a aplicação e Acessar a URL da Api em qualquer consumidor de endpoint

```
serverless deploy
```
![Screenshot from 2024-05-31 23-41-35](https://github.com/weslleysilvaa27/serverless-backend/assets/171731302/71f64613-3f54-4a3d-b9f2-7f8a276c8097)



### Dropar a aplicação
```
serverless remove
```

