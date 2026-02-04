import requests

BASE_URL = "http://127.0.0.1:8000"

# 1) login
login = requests.post(f"{BASE_URL}/login", json={"usuario": "admin", "senha": "123"})
token = login.json().get("token")
headers = {"Authorization": f"Bearer {token}"}

# 2) criar tarefa
tarefa = requests.post(
    f"{BASE_URL}/tarefas",
    json={"descricao": "Estudar FastAPI", "prioridade": "alta"},
    headers=headers,
)
print("Criar:", tarefa.status_code, tarefa.json())

# 3) listar tarefas
lista = requests.get(f"{BASE_URL}/tarefas", headers=headers)
print("Lista:", lista.status_code, lista.json())

# 4) atualizar status para 50%
if tarefa.ok:
    tarefa_id = tarefa.json().get("id")
    atualizar = requests.put(
        f"{BASE_URL}/tarefas/{tarefa_id}/status",
        json={"status": 50},
        headers=headers,
    )
    print("Atualizar:", atualizar.status_code, atualizar.json())

# 5) exemplo de erro (status invalido)
if tarefa.ok:
    atualizar_erro = requests.put(
        f"{BASE_URL}/tarefas/{tarefa_id}/status",
        json={"status": 120},
        headers=headers,
    )
    print("Erro:", atualizar_erro.status_code, atualizar_erro.json())
