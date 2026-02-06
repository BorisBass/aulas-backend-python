# Exercícios Práticos - BEP034: WebSockets e Comunicação em Tempo Real

## Exercício 1: Entender Diferenças HTTP vs WebSocket

**Objetivo:** Compreender quando usar cada protocolo.

**Tarefa:**
Para cada cenário abaixo, indique se usaria **HTTP** ou **WebSocket** e explique:

1. API REST para gerenciar produtos (CRUD)
2. Sistema de chat em tempo real
3. Dashboard com métricas atualizadas a cada segundo
4. Upload de arquivo
5. Notificações push instantâneas
6. Buscar dados de um produto específico
7. Jogo multiplayer online
8. Formulário de cadastro

---

## Exercício 2: Configurar Django Channels

**Objetivo:** Configurar ambiente para WebSockets.

**Tarefa:**
1. Instale `channels` e `channels-redis`
2. Configure no `settings.py`:
   - Adicione `channels` ao INSTALLED_APPS
   - Configure ASGI_APPLICATION
3. Crie arquivo `asgi.py` básico
4. Teste se o servidor inicia corretamente

---

## Exercício 3: Consumer Básico - Echo

**Objetivo:** Criar primeiro WebSocket que ecoa mensagens.

**Tarefa:**
1. Crie um Consumer que:
   - Aceita conexões
   - Recebe mensagens do cliente
   - Envia a mensagem de volta (echo)
2. Configure rota WebSocket
3. Crie página HTML simples com JavaScript para testar
4. Teste enviando mensagens e recebendo eco

---

## Exercício 4: Chat Simples

**Objetivo:** Criar chat básico com múltiplos usuários.

**Tarefa:**
1. Crie Consumer de chat que:
   - Adiciona usuários a um grupo
   - Recebe mensagens de qualquer usuário
   - Envia mensagem para todos no grupo
2. Inclua nome do usuário e timestamp
3. Crie interface HTML para:
   - Conectar ao WebSocket
   - Enviar mensagens
   - Exibir mensagens recebidas
4. Teste com múltiplas abas/janelas

---

## Exercício 5: Notificações em Tempo Real

**Objetivo:** Criar sistema de notificações.

**Tarefa:**
1. Crie Consumer de notificações
2. Quando um evento acontece (ex: novo pedido), envie notificação
3. Cliente recebe e exibe notificação
4. Implemente:
   - Contador de notificações não lidas
   - Marcar como lida
   - Histórico de notificações

---

## Exercício 6: Status Online/Offline

**Objetivo:** Mostrar status de usuários online.

**Tarefa:**
1. Quando usuário conecta ao WebSocket:
   - Adicione à lista de online
   - Notifique outros usuários
2. Quando usuário desconecta:
   - Remova da lista
   - Notifique outros usuários
3. Crie endpoint HTTP que retorna lista de usuários online
4. Atualize interface em tempo real

---

## Exercício 7: Salas/Canais de Chat

**Objetivo:** Criar múltiplas salas de chat.

**Tarefa:**
1. Permita que usuários entrem em diferentes salas
2. Mensagens são enviadas apenas para usuários na mesma sala
3. Implemente:
   - Listar salas disponíveis
   - Entrar em sala
   - Sair de sala
   - Enviar mensagem para sala específica

---

## Exercício 8: Autenticação em WebSocket

**Objetivo:** Autenticar conexões WebSocket.

**Tarefa:**
1. Valide token JWT na conexão WebSocket
2. Se token inválido, rejeite conexão
3. Associe usuário autenticado à conexão
4. Use informações do usuário nas mensagens
5. Teste com tokens válidos e inválidos

---

## Exercício 9: Tratamento de Erros em WebSocket

**Objetivo:** Tratar erros adequadamente.

**Tarefa:**
1. Implemente tratamento de erros no Consumer:
   - Erros de conexão
   - Erros ao processar mensagens
   - Erros de validação
2. Envie mensagens de erro ao cliente
3. Loge erros no servidor
4. Teste com dados inválidos

---

## Exercício 10: Sistema Completo - Chat com Notificações

**Objetivo:** Criar sistema completo de chat.

**Tarefa:**
Crie um sistema de chat completo com:

**Funcionalidades:**
- Múltiplas salas de chat
- Autenticação JWT
- Status online/offline
- Notificações de novas mensagens
- Histórico de mensagens
- Indicador de digitação
- Mensagens privadas

**Requisitos:**
- Consumer WebSocket bem estruturado
- Tratamento de erros
- Logs de atividades
- Interface HTML/JavaScript funcional

---

## Respostas e Soluções

As soluções detalhadas estão disponíveis no arquivo `SOLUCOES_EXERCICIOS.md`.

