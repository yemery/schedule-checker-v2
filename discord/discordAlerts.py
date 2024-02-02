import requests
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

url = f'https://discord.com/api/v10/channels/{CHANNEL_ID}/messages'
headers = {
    'Authorization': f'Bot {TOKEN}',
}

def sendAlert():
    data = {
    'content': 'Hello, Discord!',
    }
    files = {'file': ('discrod/214.png', open('discord/214.png', 'rb'), 'image/png')}

    response = requests.post(url, headers=headers, data=data,files=files)

    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print(f'Failed to send message. Status code: {response.status_code}, Response: {response.text}')



if __name__ == "__main__":
    sendAlert()