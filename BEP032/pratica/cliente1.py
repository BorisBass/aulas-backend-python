import requests


resposta = requests.get(
    "http://localhost:8000/lista")

print(resposta.status_code)
print(resposta.json())

resposta = requests.get(
    "http://localhost:8000/usuarios",
    auth=("admin", "123")
)
print(resposta.status_code)
print(resposta.json())


