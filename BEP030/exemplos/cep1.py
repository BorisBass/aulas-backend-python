import requests

try:
    resp = requests.get("https://viacep.com.br/ws/45078300/json/", timeout=5)
    resp.raise_for_status()
    dados = resp.json()
    print(resp.status_code)
    print(dados)

except requests.RequestException:
    print("Erro ao consultar o serviço ViaCEP.")


