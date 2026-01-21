import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    resp = requests.get(url, timeout=5)
    print("Status:", resp.status_code)
    if resp.status_code == 200:
        print(resp.json())
    else:
        print("Erro HTTP:", resp.text)
except requests.exceptions.Timeout:
    print("Timeout ao acessar a API")
except requests.exceptions.RequestException as e:
    print("Erro de rede:", e)