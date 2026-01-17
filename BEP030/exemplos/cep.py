import requests
import re

def limpa_formulario():
    return {
        "rua": "",
        "bairro": "",
        "cidade": "",
        "uf": "",
        "ibge": ""
    }

def consulta_cep(cep):
    # Apenas números
    cep = re.sub(r"\D", "", cep)

    if not cep:
        print("CEP vazio. Limpando dados...")
        return None

    # CEP deve ter 8 dígitos
    if not re.fullmatch(r"\d{8}", cep):
        print("Formato de CEP inválido.")
        return None

    print("Consultando CEP...")
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        dados = resp.json()

        # CEP inexistente
        if "erro" in dados:
            print("CEP não encontrado.")
            return None

        campos = {
            "rua": dados.get("logradouro", ""),
            "bairro": dados.get("bairro", ""),
            "cidade": dados.get("localidade", ""),
            "uf": dados.get("uf", ""),
            "ibge": dados.get("ibge", "")
        }

        return campos

    except requests.RequestException:
        print("Erro ao consultar o serviço ViaCEP.")
        return None


if __name__ == "__main__":
    cep = input("Digite um CEP: ").strip()
    resultado = consulta_cep(cep)

    if resultado:
        print("\nResultado:")
        print(f"Rua: {resultado['rua']}")
        print(f"Bairro: {resultado['bairro']}")
        print(f"Cidade: {resultado['cidade']}")
        print(f"Estado: {resultado['uf']}")
        print(f"IBGE: {resultado['ibge']}")
    else:
        print("\nNenhum dado a exibir.")
