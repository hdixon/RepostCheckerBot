import os

client_id = os.environ['BOT_CLIENT_ID']
client_secret = os.environ['BOT_CLIENT_SECRET']
user_agent = os.environ['BOT_USER_AGENT']
username = os.environ['BOT_USERNAME']
password = os.environ['BOT_PASSWORD']
subSettings = [
    [
        os.environ['BOT_SUBREDDIT'],
        int(os.environ['BOT_HOT_DAYS']),
        int(os.environ['BOT_NEW_DAYS']),
        int(os.environ['BOT_THRESH'])
    ],
]
