import asyncio
from telethon import TelegramClient

API_ID = 9224201
API_HASH = '4d7f17d25f8b9f15b68c1e385ff6a75e'
BOT_TOKEN = '5803383640:AAGyvj0S1q8xD-5tPKefxgPWyg_k8vKRyoc'
botClient = TelegramClient('bot_session', api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN)


async def delete_message(msg_id):
    await botClient.delete_messages(entity='me', message_ids=[msg_id])

