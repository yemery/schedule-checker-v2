import requests
from dotenv import load_dotenv
import os
load_dotenv()
# Replace 'YOUR_BOT_TOKEN' and 'CHANNEL_ID' with actual values
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

url = f'https://discord.com/api/v10/channels/{CHANNEL_ID}/messages'
headers = {
    'Authorization': f'Bot {TOKEN}',
    'Content-Type': 'application/json',
}

def sendAlert():
    data = {
    'content': 'Hello, Discord!',
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print(f'Failed to send message. Status code: {response.status_code}, Response: {response.text}')



# if __name__ == "__main__":
#     sendAlert()
