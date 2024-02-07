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

def sendAlert(group,message):
    imagePath=f"screenshots/{group}.png"
    
    data = {
    'content': f"Attention <@&?>: \n The schedule has been updated. ",
    }
    files = {'file': (imagePath, open(imagePath, 'rb'), 'image/png')}

    response = requests.post(url, headers=headers, data=data,files=files)

    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print(f'Failed to send message. Status code: {response.status_code}, Response: {response.text}')



