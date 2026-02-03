import requests

# 1) login
login = requests.post("http://localhost:8000/login", json={
    "usuario": "admin",
    "senha": "123"
})
token = login.json().get("token")

# 2) acesso protegido
headers = {"Authorization": f"Bearer {token}"}
resp = requests.get("http://localhost:8000/protegido", headers=headers)
print(resp.status_code)
print(resp.json())