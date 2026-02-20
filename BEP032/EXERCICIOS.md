# Exercícios Práticos - BEP032: Autenticação e Autorização (FastAPI)

## Exercício 1: Diferenciar Autenticação e Autorização

Identifique se cada situação é **autenticação** ou **autorização**:
1. Login com usuário e senha
2. Verificar se é admin
3. Validar token JWT
4. Bloquear acesso a deletar produtos

---

## Exercício 2: Basic Auth com FastAPI

Crie uma rota protegida usando `HTTPBasic`:
- Se credenciais inválidas, retorne 401
- Se válidas, retorne lista de usuários

---

## Exercício 3: Token simples com HTTPBearer

Crie:
- `POST /login` que gera token
- `GET /protegido` que valida token no header `Authorization: Bearer <token>`

---

## Exercício 4: JWT com OAuth2PasswordBearer

Implemente:
- Geração de JWT (`python-jose`)
- Endpoint protegido validando token
- Expiração do token

---

## Exercício 5: Autorização por role

Crie rotas onde:
- Usuários autenticados listam produtos
- Apenas admin pode criar/deletar

---

## Respostas e Soluções

As soluções detalhadas estão disponíveis em `SOLUCOES_EXERCICIOS.md`.
