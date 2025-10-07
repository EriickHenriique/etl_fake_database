import requests


url = "http://localhost:8000/gerar_compra/100"

response = requests.get(url)

print(response.json())