# GroupMe Bot - GroupMe ChatBot

## Overview

This Python script implements a basic GroupMe bot that responds to specific messages in a GroupMe group. The bot is designed to run continuously, checking for new messages and responding accordingly.

## Features

1. **Personal Greetings**
   - If a message starts with "hey bot" from the specified user, the bot responds with "sup."

2. **Time-based Responses**
   - Greets all users with "good morning" or "good night" based on the time of the day.

3. **Joke Retrieval**
   - Responds with a joke when the user sends the message "tell me a joke."

4. **Fun Facts**
   - Responds with an interesting fact when the user sends the message "tell me a fact."

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed on your machine.
- GroupMe account and a created bot in the GroupMe Developer portal.
- Ninja API Key for joke and fact retrieval.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Install dependencies:

    ```bash
    pip install requests python-dotenv
    ```

3. Create a `.env` file in the project root and add the following:

    ```env
    BOT_ID=your_groupme_bot_id
    GROUP_ID=your_groupme_group_id
    ACCESS_TOKEN=your_groupme_access_token
    API_KEY=your_ninja_api_key
    ```

## Usage

1. Run the script:

    ```bash
    python your_script_name.py
    ```

2. The script will continuously check for new messages in the specified GroupMe group and respond based on the defined features.

## Notes

- Adjust the `USER_ID` variable in the script to match the GroupMe user ID you want the bot to respond to personally.
- The script sleeps for 10 seconds between each check for new messages. You can adjust this interval based on your needs.

Feel free to customize the script, add more features, or modify the responses to suit your preferences.
