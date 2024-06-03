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
![Screenshot from 2024-05-31 23-19-42](https://github.com/WeslleySilvaa20/serverless-backend/assets/171616751/5f36d470-41da-4be0-a160-e1c65b2060be)
![Screenshot from 2024-05-31 23-22-08](https://github.com/WeslleySilvaa20/serverless-backend/assets/171616751/aed1fe3e-7e32-47d2-a5dd-56d085e38837)
![Screenshot from 2024-05-31 23-23-39](https://github.com/WeslleySilvaa20/serverless-backend/assets/171616751/190b6f9e-9921-4179-a2ea-53501b03cd92)


### Selecionar a Aba Credenciais de Segurança e criar a Chaves de acesso para obter o AccessKey e SecretKey
![Screenshot from 2024-05-31 23-24-28](https://github.com/WeslleySilvaa20/serverless-backend/assets/171616751/934327fd-176e-4326-ae7a-615c4e114b2e)


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
![Screenshot from 2024-05-31 23-41-35](https://github.com/WeslleySilvaa20/serverless-backend/assets/171616751/1eb5e512-4c8a-4b38-9ffd-934a99f7f4b5)


### Dropar a aplicação
```
serverless remove
```

