import requests

cep = "45028738"
r = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
print(r.json())


# JSONPlaceholder
resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(resp.json())