import requests
from typing import TypeVar, Generic, Type
from sqlalchemy import create_engine, insert, Table, Column, Integer, String, MetaData, Date, Float

T = TypeVar('T')


class APIOrchestrator(Generic[T]):

    def __init__(self, schema: Type[T], db_url: str, api: str, tabela_nome: str):
        self._schema = schema
        self._db = db_url
        self._api = api
        self._engine = create_engine(db_url)
        self._metadata_obj = MetaData()
        self._tabela = self._define_table(tabela_nome)
        self._metadata_obj.create_all(self._engine)
        return
    
    def start(self, param):
        response = self.getData(param)
        response = self.schemaData(response)
        response = self.insertData(response)
        return 
    
    def _define_table(self, tabela_nome: str):
        return Table( 
            tabela_nome, self._metadata_obj,
            Column("id", Integer, primary_key=True),
            Column("date_purchase", Date, nullable=False),
            Column("client_name", String(50), nullable=False),
            Column("client_lastname", String(50), nullable=False),
            Column("state", String(50)),
            Column("birthday_client", Date),
            Column("job", String(50)),
            Column("payment_type", String(50)),
            Column("store", Integer),
            Column("category", String(100)),
            Column("product", String(255)),
            Column("brand", String(100)),
            Column("price", Float)
        )


    def getData(self, param):
        response = None
        if param > 1:
            response = requests.get(f'{self._api}/{param}').json()
        else:
            response = requests.get(f'{self._api}/1').json()
        return response


    def schemaData(self, response) -> list[T]:
        if isinstance(response, dict):
            response = [response]
        elif not isinstance(response, list):
            raise ValueError(f"A API retornou um formato inesperado: {type(response)}")
        
        result = [self._schema(**item) for item in response] 
        return result

    def insertData(self, response: list[T]):
        dados_inserir = [item.model_dump() for item in response]
        try:
            with self._engine.begin() as connection:
                cmd = insert(self._tabela)
                result = connection.execute(cmd, dados_inserir)

                print(f'Sucesso! {result.rowcount} linhas inseridas após a verificação da tabela')
                return
        except Exception as e:
            print(f'Erro no pipeline de dados: {e}')  
            return

