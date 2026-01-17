import requests

BASE = "https://jsonplaceholder.typicode.com"

try:
    # GET
    r = requests.get(f"{BASE}/posts/1", timeout=5)
    r.raise_for_status()
    print("GET:", r.status_code, r.json())

    # POST
    novo = {"title": "Meu post", "body": "Conteúdo", "userId": 1}
    r = requests.post(f"{BASE}/posts", json=novo, timeout=5)
    r.raise_for_status()
    print("POST:", r.status_code, r.json())

    # PUT (substitui tudo)
    atualizado = {"id": 1, "title": "Novo título", "body": "Novo texto", "userId": 1}
    r = requests.put(f"{BASE}/posts/1", json=atualizado, timeout=5)
    r.raise_for_status()
    print("PUT:", r.status_code, r.json())

    # PATCH (atualiza parte)
    parcial = {"title": "Título parcial"}
    r = requests.patch(f"{BASE}/posts/1", json=parcial, timeout=5)
    r.raise_for_status()
    print("PATCH:", r.status_code, r.json())

    # DELETE
    r = requests.delete(f"{BASE}/posts/1", timeout=5)
    r.raise_for_status()
    print("DELETE:", r.status_code)
except requests.exceptions.Timeout:
    print("Timeout ao acessar a API")
except requests.exceptions.RequestException as e:
    print("Erro na requisição:", e)