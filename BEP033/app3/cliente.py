import requests

BASE_URL = "http://127.0.0.1:8000"

# 1) login
login = requests.post(f"{BASE_URL}/login", json={"usuario": "admin", "senha": "123"})
token = login.json().get("token")
headers = {"Authorization": f"Bearer {token}"}

# 2) criar tarefa (ok)
tarefa = requests.post(
    f"{BASE_URL}/tarefas",
    json={"descricao": "Estudar logs e erros", "prioridade": "media"},
    headers=headers,
)
print("Criar:", tarefa.status_code, tarefa.json())

# 3) criar tarefa (erro - prioridade invalida)
tarefa_erro = requests.post(
    f"{BASE_URL}/tarefas",
    json={"descricao": "Tarefa com erro", "prioridade": "urgente"},
    headers=headers,
)
print("Erro:", tarefa_erro.status_code, tarefa_erro.json())

# 4) atualizar status (erro - fora de 0 a 100)
if tarefa.ok:
    tarefa_id = tarefa.json().get("id")
    atualizar = requests.put(
        f"{BASE_URL}/tarefas/{tarefa_id}/status",
        json={"status": 150},
        headers=headers,
    )
    print("Atualizar erro:", atualizar.status_code, atualizar.json())
