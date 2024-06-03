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
![Screenshot from 2024-05-31 23-19-42](https://github.com/WeslleyAraujo97/serverless-backend/assets/171397051/fab8204c-a92b-487f-8bf6-0da63a91dc56)
![Screenshot from 2024-05-31 23-22-08](https://github.com/WeslleyAraujo97/serverless-backend/assets/171397051/1aec7169-3b0e-48fa-bcbc-4216f06d1fd2)
![Screenshot from 2024-05-31 23-23-39](https://github.com/WeslleyAraujo97/serverless-backend/assets/171397051/b93feb59-ea2e-48d0-8004-43f3cfcd3341)

### Selecionar a Aba Credenciais de Segurança e criar a Chaves de acesso para obter o AccessKey e SecretKey
![Screenshot from 2024-05-31 23-24-28](https://github.com/WeslleyAraujo97/serverless-backend/assets/171397051/fd2a6584-3dc9-408d-8ad2-e4a50f274f8b)

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
![Screenshot from 2024-05-31 23-41-35](https://github.com/WeslleyAraujo97/serverless-backend/assets/171397051/66d2bde4-45e3-4261-8083-f740806d3fdc)

### Dropar a aplicação
```
serverless remove
```

