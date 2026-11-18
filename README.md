# CRUD API

Projeto de estudo com FastAPI, SQLAlchemy, Alembic e PostgreSQL.

## Estrutura

```text
app/
├── main.py          # Criação da aplicação e registro das rotas
├── routes/          # Endpoints HTTP
├── schemas/         # Validação de entrada e respostas (Pydantic)
├── models/          # Tabelas e relacionamentos (SQLAlchemy)
├── services/        # Operações e regras de negócio
├── db/
│   ├── base.py      # Base dos modelos SQLAlchemy
│   └── session.py   # Espaço para configurar conexão e sessões
└── core/
    └── config.py    # Espaço para configurar variáveis de ambiente
tests/              # Testes automatizados
```

Os pacotes incluem `__init__.py`. As pastas ainda vazias serão preenchidas durante o treino, começando por clientes e depois produtos.

## Executar

Com uv instalado, na raiz do projeto:

```bash
uv sync
uv run uvicorn app.main:app --reload
```

- Documentação interativa: http://127.0.0.1:8000/docs
- Verificação da API: http://127.0.0.1:8000/health

## Verificar

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

## Próximas etapas

1. Configurar PostgreSQL e a leitura de `DATABASE_URL` em `core/config.py`.
2. Configurar engine e sessões em `db/session.py`.
3. Inicializar Alembic, criando `migrations/` e `alembic.ini`, e vinculá-lo à metadata de `Base`.
4. Implementar modelos, schemas, serviços e rotas de clientes.
5. Criar e aplicar a primeira migração e testar o CRUD.

A aplicação atual não se conecta ao banco. `.env.example` é apenas uma referência: copie para `.env` quando implementarmos a configuração. Não envie senhas reais ao Git. `/health` verifica somente a resposta HTTP da API.
