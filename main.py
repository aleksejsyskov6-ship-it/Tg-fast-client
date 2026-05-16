import os
from telethon import TelegramClient
import asyncio

# Загружаем секретные переменные
API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')
PHONE = os.environ.get('PHONE')

async def main():
    # Создаём клиента
    client = TelegramClient(
        'session', 
        API_ID, 
        API_HASH
    )
    
    await client.start(phone=PHONE)
    print("🚀 Клиент успешно запущен!")
    
    me = await client.get_me()
    print(f"Имя: {me.first_name}")
    print(f"Username: @{me.username}")
    
    await client.disconnect()

asyncio.run(main())
