import os
from telethon import TelegramClient
from telethon.network import ConnectionTcpMTProxyWS
import asyncio

# Загружаем секретные переменные
API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')

async def main():
    # Создаём клиента с WebSocket (чтобы летал)
    client = TelegramClient(
        'session', 
        API_ID, 
        API_HASH,
        connection=ConnectionTcpMTProxyWS
    )
    
    await client.start()
    print("🚀 Клиент успешно запущен через WebSocket!")
    
    me = await client.get_me()
    print(f"Имя: {me.first_name}")
    print(f"Username: @{me.username}")
    
    await client.disconnect()

asyncio.run(main())
