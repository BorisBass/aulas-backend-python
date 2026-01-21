#pip install requests
import requests

resp = requests.get("https://viacep.com.br/ws/00000000/json/")
dados = resp.json()
print(resp.status_code)
#print(dados)