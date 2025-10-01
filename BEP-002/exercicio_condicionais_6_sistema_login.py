# Exercício 6: Sistema de Login
# Crie um sistema de login simples:
# 1. Solicite usuário e senha
# 2. Verifique se o usuário existe (usuário: "admin", senha: "123456")
# 3. Exiba mensagens apropriadas:
#    - "Login realizado com sucesso!"
#    - "Usuário incorreto!"
#    - "Senha incorreta!"

print("=== SISTEMA DE LOGIN ===")
print()

# Dados de acesso válidos
validUsername = "admin"
validPassword = "123456"

# Entrada de dados
username = input("Digite seu usuário: ")
password = input("Digite sua senha: ")

# Estrutura condicional para verificação de login
print()
print("=== VERIFICAÇÃO DE LOGIN ===")
print(f"Usuário informado: {username}")
print("Senha: [oculta por segurança]")
print()

if username == validUsername:
    if password == validPassword:
        print("✅ LOGIN REALIZADO COM SUCESSO!")
        print("Bem-vindo ao sistema!")
        print("Você tem acesso a todas as funcionalidades.")
    else:
        print("❌ SENHA INCORRETA!")
        print("A senha informada não confere com o usuário.")
        print("Tente novamente.")
else:
    print("❌ USUÁRIO INCORRETO!")
    print("O usuário informado não existe no sistema.")
    print("Verifique se digitou corretamente.")

# Informações adicionais
print()
print("=== INFORMAÇÕES ADICIONAIS ===")
print("Dicas de segurança:")
print("- Mantenha suas credenciais em local seguro")
print("- Use senhas fortes e únicas")
print("- Não compartilhe suas informações de acesso")
print()
print("Status da verificação:")
print(f"- Usuário válido: {'Sim' if username == validUsername else 'Não'}")
print(f"- Senha válida: {'Sim' if password == validPassword else 'Não'}")
print(f"- Login autorizado: {'Sim' if username == validUsername and password == validPassword else 'Não'}")

# Demonstração de operadores lógicos
print()
print("=== DEMONSTRAÇÃO DE OPERADORES LÓGICOS ===")
print("Verificação usando operadores lógicos:")
print(f"username == validUsername: {username == validUsername}")
print(f"password == validPassword: {password == validPassword}")
print(f"username == validUsername and password == validPassword: {username == validUsername and password == validPassword}")

