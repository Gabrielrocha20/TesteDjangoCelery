# **Documentação da API**

Bem-vindo à documentação da API do Teste Prático. Este repositório aborda a implementação de um projeto de teste prático.

O projeto consiste em um backend Django com integração Celery e Redis, enquanto o frontend é desenvolvido em React.

## **Modelos**

### **1. Campo Proposta**

O modelo **`Campo Proposta`** permite que os administradores cadastrem perguntas. Cada pergunta pode ter atributos como:

- Nome
- Me diga sobre você?

Dentro desse modelo, é possível especificar diferentes tipos de formatos de dados:

- Texto
- Arquivo
- Imagem
- Booleano

Para o propósito deste projeto, estaremos trabalhando exclusivamente com o formato de Texto. É recomendado criar sempre uma pergunta chamada "Nome", onde os usuários podem fornecer seus nomes. Outras perguntas podem ser personalizadas pelo administrador.

### **2. Valor Campo**

O modelo **`Valor Campo`** é responsável por armazenar tanto perguntas quanto respostas dos usuários.

### **3. Propostas**

O modelo **`Propostas`** representa as propostas aceitas pela API. Ele contém uma referência ao correspondente **`Valor Campo`**.

## **Endpoints da API**

### **GET /propostas/api/v1/**

Este endpoint recupera todas as propostas salvas.
### **GET /propostas/api/v1/<int:id>/**

Este endpoint recupera uma proposta com id informado pela url

### **GET /propostas/api/v1/campo-proposta/**

Este endpoint fornece todas as perguntas criadas pelos administradores no painel de controle (ADM).

### **POST /propostas/api/v1/register/**

Este é um endpoint crucial, onde o frontend precisa enviar um payload JSON no seguinte formato:

```json

{
  "nome": "nome_do_usuário",
  "campos_valores": [
    {
      "campo": "id_da_pergunta",
      "pergunta": "resposta_do_usuário"
    }
  ]
}

```

Ao fazer uma solicitação POST, os dados do usuário serão salvos nas propostas aceitas. Posteriormente, uma tarefa do Celery será acionada. Essa tarefa tem como objetivo enviar os dados para a API de verificação. Se a API de verificação retornar Verdadeiro (True), os dados permanecerão armazenados. No entanto, se retornar Falso (False), os dados serão excluídos.

Observação: Por padrão, o Django sempre retorna Verdadeiro (True) para solicitações. O processo de verificação ocorre em uma fila e será processado como tarefas.

## **Contêiner Docker**

Para simplificar o processo de teste sem a necessidade de baixar este repositório e instalar as dependências, você pode usar o contêiner Docker fornecido.

Observe que o Celery não funciona no Windows, portanto, é recomendável usar o Docker para uma experiência mais tranquila.

# Exemplo de Docker Compose para Aplicação Multi-Container

Este é um exemplo de arquivo `docker-compose.yml` que ilustra como executar vários serviços como contêineres Docker usando o Docker Compose. Neste exemplo, as imagens são criadas a partir de `gabrielrocha20/testedjango:redis`, `gabrielrocha20/testedjango:django`, `gabrielrocha20/testedjango:celery` e `gabrielrocha20/testedjango:react`.

Certifique-se de ajustar as configurações, imagens e variáveis de ambiente de acordo com suas necessidades.

```yaml
version: '3'
services:
  redis:
    image: gabrielrocha20/testedjango:redis

  django:
    image: gabrielrocha20/testedjango:django
    ports:
      - "8000:8000"
    depends_on:
      - redis
    environment:
      - DEBUG=1
      - DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
      - CELERY_BROKER=redis://redis:6379/0
      - CELERY_BACKEND=redis://redis:6379/0

  celery:
    image: gabrielrocha20/testedjango:celery
    depends_on:
      - redis
      - django
    environment:
      - DEBUG=1
      - DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
      - CELERY_BROKER=redis://redis:6379/0
      - CELERY_BACKEND=redis://redis:6379/0

  react:
    image: gabrielrocha20/testedjango:react
    ports:
      - "3000:3000"
    environment:
      - REACT_APP_API_URL=http://localhost:8000
```

aqui esta o link de cada imagem do docker
docker pull gabrielrocha20/testedjango:redis
docker pull gabrielrocha20/testedjango:django
docker pull gabrielrocha20/testedjango:celery
docker pull gabrielrocha20/testedjango:react