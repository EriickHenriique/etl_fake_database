from backend.APIOrchestrator import APIOrchestrator
from backend.contracts.contracts import CompraSchema
import time

#Usando LocalHost do Docker
api = 'http://fastapi:8000/gerar_compra'
db = f"postgresql+psycopg2://postgres:postgres@postgres:5432/etl_fakedata"

#Chamando a Classe APIOrchestrator e passando os parâmetros
extract = APIOrchestrator(
    schema=CompraSchema,
    db_url=db,
    api=api,
    tabela_nome='tabela_compras')

#Constants
NUM_ITERATIONS = 50
DELAY_SECONDS = 5
RECORDS_PER_RUN = 10000

#Iniciando o Loop de Extração de Dados
print(f'Iniciando o ETL: {RECORDS_PER_RUN} registros por execução, repetindo {NUM_ITERATIONS} a cada {DELAY_SECONDS} segundos')

total_elapsed_seconds = 0.0

for i in range(1, NUM_ITERATIONS + 1):
    start_time = time.time()
    print(f'Início da Extração {i}/{NUM_ITERATIONS}')  
    extract.start(RECORDS_PER_RUN)
    end_time = time.time()
    elapsed = end_time - start_time
    total_elapsed_seconds += elapsed 
    print(f'Fim da Extração {i}/{NUM_ITERATIONS}')
    print(f"Extração {i} concluída em {elapsed:.2f} segundos.")
    if i < NUM_ITERATIONS:
        print(f"Aguardando {DELAY_SECONDS} segundos para a próxima rodada...")
        time.sleep(DELAY_SECONDS)
        total_elapsed_seconds += DELAY_SECONDS 


formatted_time_short = time.strftime("%H:%M:%S", time.gmtime(total_elapsed_seconds))

print(f'ETL Concluída com Sucesso em: {formatted_time_short}')