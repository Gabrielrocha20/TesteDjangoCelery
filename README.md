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

### **GET /propostas**

Este endpoint recupera todas as propostas salvas.

### **GET /campo_proposta**

Este endpoint fornece todas as perguntas criadas pelos administradores no painel de controle (ADM).

### **POST /register**

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

Sinta-se à vontade para usar esta documentação como referência ao interagir com a API. Se encontrar problemas ou tiver dúvidas, não hesite em pedir assistência. Feliz teste!

Ola este repositorio e sobre o Teste pratico

o projeto foi feito o Back end em Django, celery e redis e o frontend foi feito em React

Temos 3 Models criados

Proposta, Campo proposta e Valor_campo

1 - Campo proposta e um model onde o ADM vai poder cadastrar perguntas como

Nome

Me diga sobre voce?

no model temos a possibilidade de cadastrar esses tipos de arquivo

Texto, Arquivo, Image, Bollean

o ADM podera escolher o tipo de dado que ele quer receber porem Vamos trabalhar apenas com Texto

Sempre que usar, crie uma pergunta chamada "Nome", que será onde o usuário enviará seu nome.

As demais perguntas, o ADM poderá escolher o que escrever.

2- Valor_campo Este modelo será responsável por armazenar as perguntas e respostas do usuário.

3 - Propostas seram as propostas aceitas pela api 

e onde ficara salvo o Valor_campo

## Api

Get Proposta

- essa url vai trazer todos as propostas salvas

Get Campo Proposta

- esta url vai trazer para voce todas as perguntas criadas pelo ADM no back office(pagina do ADM)

Post Register

- esta url e a mais importante nela o front end precisara enviar um json nesse formato

{

“nome”: nome do usuario,

“campos_valores”: [

{

campo: id da pergunta,

pergunta: resposta

}

]

}

Assim que fizer o post o os dados enviados pelo usuario sera salvo em propostas aceitas

e logo depois sera chamado a task do celery onde ela tem a função de enviar os dados para a api de verificação e se ela retornar True os dados continuaram la porem se ela retornar False os dados vao ser deletados

o django por padrao sempre retornara True quando fizerem a requisição, e ela mesmo entrara em uma fila ate ser verificada

pra começar voce pode usar esse container docker para testar a aplicação sem baixar este repositorio e ter que instalar as dependencias

AVISO - O celery nao esta funcionando no windowns entao usar o docker ja facilita o processo