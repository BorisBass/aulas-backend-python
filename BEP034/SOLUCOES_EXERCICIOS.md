# Soluções - Exercícios BEP034: WebSockets e Comunicação em Tempo Real

## Exercício 1: Entender Diferenças HTTP vs WebSocket

1. **API REST para gerenciar produtos** → **HTTP**
   - Operações CRUD tradicionais, não precisa tempo real

2. **Sistema de chat em tempo real** → **WebSocket**
   - Mensagens precisam chegar instantaneamente

3. **Dashboard com métricas atualizadas** → **WebSocket**
   - Atualizações frequentes em tempo real

4. **Upload de arquivo** → **HTTP**
   - Operação única, não precisa conexão persistente

5. **Notificações push instantâneas** → **WebSocket**
   - Servidor precisa enviar sem requisição do cliente

6. **Buscar dados de produto** → **HTTP**
   - Requisição única, resposta única

7. **Jogo multiplayer online** → **WebSocket**
   - Sincronização constante entre jogadores

8. **Formulário de cadastro** → **HTTP**
   - Submit único, não precisa tempo real

---

## Exercício 2: Configurar Django Channels

```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',  # Adicionar
    'app',
]

ASGI_APPLICATION = 'projeto.asgi.application'

# asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([]),  # Será configurado depois
})
```

---

## Exercício 3: Consumer Básico - Echo

```python
# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class EchoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            'mensagem': 'Conectado! Envie uma mensagem.'
        }))
    
    async def disconnect(self, close_code):
        pass
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        mensagem = data.get('mensagem', '')
        
        # Echo - enviar de volta
        await self.send(text_data=json.dumps({
            'mensagem': f'Echo: {mensagem}'
        }))

# routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/echo/$', consumers.EchoConsumer.as_asgi()),
]

# asgi.py
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from app.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})
```

---

## Exercício 4: Chat Simples

```python
# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'chat_geral'
        self.room_group_name = f'chat_{self.room_name}'
        
        # Entrar no grupo
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
    
    async def disconnect(self, close_code):
        # Sair do grupo
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        mensagem = data.get('mensagem', '')
        usuario = data.get('usuario', 'Anônimo')
        
        # Enviar para todos no grupo
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'mensagem': mensagem,
                'usuario': usuario,
                'timestamp': datetime.now().isoformat()
            }
        )
    
    async def chat_message(self, event):
        # Enviar mensagem para o cliente
        await self.send(text_data=json.dumps({
            'mensagem': event['mensagem'],
            'usuario': event['usuario'],
            'timestamp': event['timestamp']
        }))
```

---

## Exercício 5: Notificações em Tempo Real

```python
# consumers.py
class NotificacaoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.group_name = f'notificacoes_{self.user.id}'
        
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        
        await self.accept()
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
    
    async def notificacao_message(self, event):
        await self.send(text_data=json.dumps({
            'tipo': 'notificacao',
            'titulo': event['titulo'],
            'mensagem': event['mensagem'],
            'timestamp': event['timestamp']
        }))

# views.py - Enviar notificação
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def enviar_notificacao(usuario_id, titulo, mensagem):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'notificacoes_{usuario_id}',
        {
            'type': 'notificacao_message',
            'titulo': titulo,
            'mensagem': mensagem,
            'timestamp': datetime.now().isoformat()
        }
    )
```

---

## Exercício 6: Status Online/Offline

```python
# consumers.py
USUARIOS_ONLINE = set()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.room_group_name = 'chat_geral'
        
        # Adicionar à lista de online
        USUARIOS_ONLINE.add(self.user.id)
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        # Notificar outros sobre novo usuário online
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'usuario_status',
                'usuario_id': self.user.id,
                'usuario_nome': self.user.username,
                'status': 'online',
                'usuarios_online': list(USUARIOS_ONLINE)
            }
        )
    
    async def disconnect(self, close_code):
        # Remover da lista
        USUARIOS_ONLINE.discard(self.user.id)
        
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
        # Notificar outros sobre usuário offline
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'usuario_status',
                'usuario_id': self.user.id,
                'usuario_nome': self.user.username,
                'status': 'offline',
                'usuarios_online': list(USUARIOS_ONLINE)
            }
        )
    
    async def usuario_status(self, event):
        await self.send(text_data=json.dumps({
            'tipo': 'status',
            'usuario_id': event['usuario_id'],
            'usuario_nome': event['usuario_nome'],
            'status': event['status'],
            'usuarios_online': event['usuarios_online']
        }))
```

---

## Exercício 7: Salas/Canais de Chat

```python
# consumers.py
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.sala_nome = self.scope['url_route']['kwargs']['sala_nome']
        self.room_group_name = f'chat_{self.sala_nome}'
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        acao = data.get('acao')
        
        if acao == 'entrar_sala':
            nova_sala = data.get('sala')
            # Sair da sala atual
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )
            # Entrar na nova sala
            self.sala_nome = nova_sala
            self.room_group_name = f'chat_{nova_sala}'
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
        
        elif acao == 'enviar_mensagem':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'mensagem': data['mensagem'],
                    'usuario': data['usuario']
                }
            )
```

---

## Exercício 8: Autenticação em WebSocket

```python
# consumers.py
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Verificar autenticação
        self.user = self.scope['user']
        
        if isinstance(self.user, AnonymousUser):
            await self.close(code=4001)  # Não autenticado
            return
        
        # Verificar token se necessário
        query_string = self.scope.get('query_string', b'').decode()
        if 'token=' in query_string:
            token = query_string.split('token=')[1].split('&')[0]
            user = await self.validar_token(token)
            if not user:
                await self.close(code=4001)
                return
            self.user = user
        
        self.room_group_name = f'chat_{self.user.id}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
    
    @database_sync_to_async
    def validar_token(self, token):
        # Validar token JWT
        from rest_framework_simplejwt.tokens import AccessToken
        try:
            access_token = AccessToken(token)
            from django.contrib.auth import get_user_model
            User = get_user_model()
            return User.objects.get(id=access_token['user_id'])
        except:
            return None
```

---

## Exercício 9: Tratamento de Erros em WebSocket

```python
# consumers.py
import logging

logger = logging.getLogger('api')

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            await self.accept()
        except Exception as e:
            logger.error(f"Erro ao conectar: {str(e)}")
            await self.close(code=4000)
    
    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                'erro': 'JSON inválido',
                'codigo': 'JSON_INVALIDO'
            }))
            return
        
        try:
            mensagem = data.get('mensagem', '')
            if not mensagem:
                await self.send(text_data=json.dumps({
                    'erro': 'Mensagem é obrigatória',
                    'codigo': 'MENSAGEM_OBRIGATORIA'
                }))
                return
            
            # Processar mensagem
            await self.channel_layer.group_send(...)
        
        except Exception as e:
            logger.error(f"Erro ao processar mensagem: {str(e)}", exc_info=True)
            await self.send(text_data=json.dumps({
                'erro': 'Erro ao processar mensagem',
                'codigo': 'ERRO_PROCESSAMENTO'
            }))
```

---

## Exercício 10: Sistema Completo - Chat com Notificações

```python
# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from datetime import datetime
import json
import logging

logger = logging.getLogger('api')

class ChatCompletoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.sala_atual = None
        
        await self.accept()
        await self.send(text_data=json.dumps({
            'tipo': 'conectado',
            'mensagem': 'Conectado ao chat'
        }))
    
    async def disconnect(self, close_code):
        if self.sala_atual:
            await self.channel_layer.group_discard(
                f'chat_{self.sala_atual}',
                self.channel_name
            )
    
    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            acao = data.get('acao')
            
            if acao == 'entrar_sala':
                await self.entrar_sala(data.get('sala'))
            elif acao == 'enviar_mensagem':
                await self.enviar_mensagem(data.get('mensagem'))
            elif acao == 'digitar':
                await self.indicar_digitar()
            elif acao == 'parar_digitar':
                await self.parar_digitar()
        
        except Exception as e:
            logger.error(f"Erro: {str(e)}", exc_info=True)
            await self.send(text_data=json.dumps({
                'tipo': 'erro',
                'mensagem': 'Erro ao processar'
            }))
    
    async def entrar_sala(self, sala_nome):
        # Sair da sala anterior
        if self.sala_atual:
            await self.channel_layer.group_discard(
                f'chat_{self.sala_atual}',
                self.channel_name
            )
        
        # Entrar na nova sala
        self.sala_atual = sala_nome
        await self.channel_layer.group_add(
            f'chat_{sala_nome}',
            self.channel_name
        )
        
        await self.send(text_data=json.dumps({
            'tipo': 'sala_entrada',
            'sala': sala_nome
        }))
    
    async def enviar_mensagem(self, mensagem):
        if not self.sala_atual:
            await self.send(text_data=json.dumps({
                'tipo': 'erro',
                'mensagem': 'Você precisa entrar em uma sala primeiro'
            }))
            return
        
        await self.channel_layer.group_send(
            f'chat_{self.sala_atual}',
            {
                'type': 'chat_message',
                'mensagem': mensagem,
                'usuario': self.user.username,
                'timestamp': datetime.now().isoformat()
            }
        )
    
    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'tipo': 'mensagem',
            'mensagem': event['mensagem'],
            'usuario': event['usuario'],
            'timestamp': event['timestamp']
        }))
```

