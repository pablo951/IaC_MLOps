# Projeto - MLOps com IaC: Automação de Deploy de Modelo de Machine Learning na Nuvem

Este projeto demonstra como automatizar o deploy de um modelo de Machine Learning na nuvem utilizando práticas de MLOps com Infraestrutura como Código (IaC), Docker e Terraform.

## Pré-requisitos

- Docker instalado
- Conta e credenciais da AWS configuradas
- Terraform instalado

---

## 1. Preparação do Ambiente

Abra o terminal ou prompt de comando e navegue até a pasta onde os arquivos do projeto estão localizados.  
**Importante:** evite usar espaços ou acentos no nome das pastas.

---

## 2. Construção da Imagem Docker

Execute o comando abaixo para criar a imagem Docker:

```bash
docker build -t mlops-image:p7 .
```

---

## 3. Criação do Container Docker

No Linux/macOS:

```bash
docker run -dit --name mlops-p7 -v ./IaC:/iac mlops-image:p7 /bin/bash
```

No Windows (substitua o caminho conforme seu diretório):

```bash

docker run -dit --name mlops-p7 -v ./IaC:/iac mlops-image:p7 /bin/bash
```

> **Nota:** NOTA: No Windows você deve substituir ./IaC pelo caminho completo da pasta, por exemplo: (C:\Users\Cap15\IaC).

Após iniciar o container, entre no terminal do mesmo e digite:

```bash
bash
```

Verifique se as pastas foram corretamente montadas.

---

## 4. Configuração da AWS CLI

Configure o acesso à AWS com o comando:

```bash
aws configure
```

Insira:

- Chave de acesso
- Chave secreta
- Região (ex: `us-east-1`)
- Formato de saída (pressione Enter para deixar em branco)

Para testar a conexão com a AWS:

```bash
aws s3 ls
```

Se não aparecer erro, a configuração está correta.

---

## 5. Uso do Terraform

Dentro da pasta `deploy`, execute os seguintes comandos:

```bash
terraform init          # Inicializa o projeto Terraform
terraform validate      # (Opcional) Valida a sintaxe dos arquivos
terraform plan          # (Opcional) Mostra o que será criado
terraform apply         # Aplica as configurações e cria os recursos
```

Para destruir a infraestrutura criada:

```bash
terraform destroy
```

---

## 6. Acesso à Aplicação

Após o deploy, acesse o modelo via navegador pelo link gerado no processo do `terraform apply`:

```
http://<link_gerado>:5000
```

(Substitua `<link_gerado>` pelo IP ou DNS retornado, `:5000` é a porta configurada.)

---

## Licença

Este projeto é de uso livre para fins educacionais.