## Exemplo de tratamento interno de erro 500

Este exemplo mostra como tratar um erro interno na API de forma segura:

- registrar o erro no log (para quem mantem o sistema);
- devolver uma mensagem simples ao cliente (sem expor detalhes);
- usar `HTTPException` com `status_code=500`.

### Codigo exemplo (FastAPI)

```python
import logging
from fastapi import FastAPI, HTTPException

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/relatorio")
def gerar_relatorio():
    try:
        # simula algo que pode dar erro
        resultado = 10 / 0
        return {"relatorio": resultado}
    except Exception:
        logging.exception("Erro ao gerar relatorio")
        raise HTTPException(
            status_code=500,
            detail="Erro interno ao gerar relatorio. Tente novamente mais tarde."
        )
```

### O que este tratamento resolve

- O servidor continua respondendo com uma mensagem clara.
- O erro fica registrado no log para analise posterior.
- O cliente nao recebe detalhes sensiveis do erro.
