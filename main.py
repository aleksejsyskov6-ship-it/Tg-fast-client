import os
from telethon import TelegramClient
import asyncio

# Загружаем секретные переменные
API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')

async def main():
    client = TelegramClient('session', API_ID, API_HASH)
    await client.start()
    print("Клиент успешно запущен через WebSocket!")
    me = await client.get_me()
    print(f"Имя: {me.first_name}")
    await client.disconnect()

asyncio.run(main())
