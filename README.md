
# API Django de Gerenciamento de Produtos

Esta é uma API Django simples para gerenciar produtos em um sistema de estoque.

## Funcionalidades

- Listar todos os produtos
- Obter detalhes de um produto por ID
- Criar um novo produto
- Atualizar informações de um produto existente
- Excluir um produto

## Tecnologias Utilizadas

- Django
- Django REST Framework
- Python 3.x

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/api-django-estoque.git
```

2. Navegue até o diretório do projeto:

```bash
cd api-django-estoque
```

3. Crie e ative um ambiente virtual (recomendado):

```bash
python -m venv venv
```

No Windows:

```bash
venv\Scripts\activate
```

No Linux/Mac:

```bash
source venv/bin/activate
```

4. Instale as dependências do Python:

```bash
pip install -r requirements.txt
```

5. Execute as migrações do banco de dados:

```bash
python manage.py migrate
```

6. Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

A API estará disponível em `http://localhost:8000/`.

## Rotas da API

### Listar Todos os Produtos

- **URL:** `/api/`
- **Método:** `GET`
- **Retorno:**

```json
[
    {
        "id": 1,
        "nome": "Produto A",
        "quantidade": 10,
        "preco": 29.99
    },
    {
        "id": 2,
        "nome": "Produto B",
        "quantidade": 5,
        "preco": 49.99
    }
]
```

### Obter Detalhes de um Produto por ID

- **URL:** `/api/produto/{id}/`
- **Método:** `GET`
- **Retorno:**

```json
{
    "id": 1,
    "nome": "Produto A",
    "quantidade": 10,
    "preco": 29.99
}
```

### Criar um Novo Produto

- **URL:** `/api/data/`
- **Método:** `POST`
- **Corpo da Requisição:**

```json
{
    "nome": "Novo Produto",
    "quantidade": 20,
    "preco": 39.99
}
```

### Atualizar Informações de um Produto Existente

- **URL:** `/api/produto/{id}/`
- **Método:** `PUT`
- **Corpo da Requisição:**

```json
{
    "nome": "Produto Atualizado",
    "quantidade": 15,
    "preco": 34.99
}
```

### Excluir um Produto

- **URL:** `/api/produto/{id}/`
- **Método:** `DELETE`

## Contribuindo

Sinta-se à vontade para contribuir com novas funcionalidades, correções de bugs ou melhorias de documentação. Abra uma issue ou envie um pull request!

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---
