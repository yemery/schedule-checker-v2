import requests
from dotenv import load_dotenv
import os
from utils import generateColor
from dbConn import conn_db
import time

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
GUILD = os.getenv("guild")
url = f"https://discord.com/api/v10/guilds/{GUILD}/roles"
headers = {
    "Authorization": f"Bot {TOKEN}",
    "Content-Type": "application/json",
}


def getRoles():
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # print('Message sent successfully!',response.json())
        return response.json()
    else:
        # print(f'Failed to send message. Status code: {response.status_code}, Response: {response.text}')
        return None


def addRole(groupName, color):

    data = {"name": groupName, "color": color}

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(
            f"Failed to send message. Status code: {response.status_code}, Response: {response.text}"
        )


def addAllRoles():
    db = conn_db()
    if db != None:
        groups = db.groups.find()
        for group in groups:
            addRole(group["value"], generateColor())
            time.sleep(10)


if __name__ == "__main__":

    # getRoles()
    # print(generateRGBColor())
    # addRole("test",generateColor())
    addAllRoles()
