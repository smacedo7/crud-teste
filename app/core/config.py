"""As configurações e a leitura das variáveis de ambiente ficarão aqui."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    '''
    a aplicacao precisa receber uma configuracao de banco de dados,
    que sera lida do arquivo .env
    1. criar um arquivo .env na raiz do projeto
    2. adicionar a variavel DATABASE_URL com a url de conexao do banco de dados
    3. adicionar a url de conexao do banco de dados no arquivo .env
    '''
    database_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
