import requests
import time
import json
import os
from dotenv import load_dotenv

load_dotenv()

BOT_ID = os.getenv("BOT_ID")
GROUP_ID = os.getenv("GROUP_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
LAST_MESSAGE_ID = None
USER_ID = "96346276"
API_KEY = os.getenv("API_KEY")


def send_message(text, attachments=None):
    """Send a message to the group using the bot."""
    post_url = "https://api.groupme.com/v3/bots/post"
    data = {"bot_id": BOT_ID, "text": text, "attachments": attachments or []}
    response = requests.post(post_url, json=data)
    return response.status_code == 202


def get_group_messages(since_id=None):
    """Retrieve recent messages from the group."""
    params = {"token": ACCESS_TOKEN}
    if since_id:
        params["since_id"] = since_id

    get_url = f"https://api.groupme.com/v3/groups/{GROUP_ID}/messages"
    response = requests.get(get_url, params=params)
    if response.status_code == 200:
        # this shows how to use the .get() method to get specifically the messages but there is more you can do (hint: sample.json)
        return response.json().get("response", {}).get("messages", [])
    return []


def process_message(message):
    """Process and respond to a message."""
    global LAST_MESSAGE_ID
    text = message["text"].lower()
    name = message["name"]
    sender_id = message["sender_id"]
    print(name)
    print(text)
    print(message)
    
    # Dont respond to any bots!
    if message["sender_type"] != "bot":
        # TASK 1: Respond to just me
        if sender_id == USER_ID and text == "hey bot":
            send_message("sup")

        # TASK 2: respond good morning/night to anyone
        if sender_id != "system":   
            if "good morning" == text:
                send_message(f"good morning, {name}")
            elif "good night" == text:
                send_message(f"good night, {name}")

        # TASK 3: new functionality- prompt bot to tell you a joke
        if text == "tell me a joke":
            send_message(get_joke())

        # EXTRA CREDIT
        if text == "tell me a fact":
            send_message(get_fact())
        

    LAST_MESSAGE_ID = message["id"]

def get_joke():
    #use ninja API to retreive a joke and send it into the chat
    api_url = 'https://api.api-ninjas.com/v1/jokes?limit=1'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    return response.json()[0]["joke"]

def get_fact():
    api_url = 'https://api.api-ninjas.com/v1/facts?limit=1'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    return response.json()[0]["fact"]


def main():
    global LAST_MESSAGE_ID
    # this is an infinite loop that will try to read (potentially) new messages every 10 seconds, but you can change this to run only once or whatever you want
    while True:
        messages = get_group_messages(LAST_MESSAGE_ID)
        for message in reversed(messages):
            process_message(message)
        time.sleep(10)


if __name__ == "__main__":
    main()
