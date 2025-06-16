from telethon import TelegramClient, events
import re
import asyncio
from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
channel_username = os.getenv('CHANNEL_USERNAME')
call_user = os.getenv('CALL_USER')
call_user2 = os.getenv('CALL_USER2')

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=channel_username))
async def handler(event):
    message = event.message.message

    buycall = re.search(r'Buy', message, re.IGNORECASE)
    sellcall = re.search(r'Sell', message, re.IGNORECASE)

    if buycall:
        response = requests.get(f"http://api.callmebot.com/start.php?user={call_user}&text=BUY%20CALL%20INCOMING&lang=en-US-Standard-B")
        response2 = requests.get(f"http://api.callmebot.com/start.php?user={call_user2}&text=BUY%20CALL%20INCOMING&lang=en-US-Standard-B")
        print(response+"\nDhruv\n"+response2)
    elif sellcall:
        response = requests.get(f"http://api.callmebot.com/start.php?user={call_user}&text=SELL%20CALL%20INCOMING&lang=en-US-Standard-B")
        response2 = requests.get(f"http://api.callmebot.com/start.php?user={call_user2}&text=SELL%20CALL%20INCOMING&lang=en-US-Standard-B")
        print(response+"\nDhruv\n"+response2)
    else:
        print(message)
    
    

async def main():
    while True:
        await client.start()
        await client.run_until_disconnected()

asyncio.run(main())

