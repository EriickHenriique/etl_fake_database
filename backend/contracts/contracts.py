from pydantic import BaseModel
from datetime import date


#Criando Schema utilizando Pydantic
class CompraSchema(BaseModel):
    date_purchase: date
    client_name: str
    client_lastname: str
    state: str
    birthday_client: date
    job: str
    payment_type: str
    store: int
    category: str
    product: str
    brand: str
    price: float