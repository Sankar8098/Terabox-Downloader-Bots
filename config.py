from os import environ

# config.py

# Telegram API credentials
API_ID = '23990433'  # Replace with your API ID
API_HASH = 'e6c4b6ee1933711bc4da9d7d17e1eb20'  # Replace with your API Hash
BOT_TOKEN = '5811431199:AAEN_0Az6QE_E8HCvJM7JhD0WqPobmRHK2k'  # Replace with your bot token

# Redis database credentials
HOST = 'redis-15392.c304.europe-west1-2.gce.cloud.redislabs.com'  # Replace with your Redis host
PORT = 6379  # Default Redis port is 6379
PASSWORD = 'cbw7xHuW3uJmddWJRRqxiSWmRvKi81GM'  # Replace with your Redis password

# Private chat ID where media files will be sent and stored
PRIVATE_CHAT_ID = '-1001571491517'  # Replace with your private chat ID

# List of admin user IDs who can use admin commands
ADMINS = [
    5821871362,  # Replace with Telegram user IDs of the admins
    987654321
]

# Other settings (if any)
# Add any other configuration variables you need here


# Config
COOKIE = environ.get("COOKIE", "csrfToken=BnQx-ffuJKamkWLrsx3Ksds4; browserid=qEGrcJcpudjTVSp34yywiOK8KGczvjGYTPI6jJMydd7dpoQVUXCzDlp7JFM=; lang=en; __bid_n=18db31bdad1e0ee8094207; __stripe_mid=a300821a-4b38-4e0a-a227-5c27f1b7c54789f06e; __stripe_sid=f7b244b5-18a8-4540-bfa0-222b4acc0bf5eb56ba; ndus=Yb47bKTteHuiwDuAJYscQHtlthgbg2-2R4yRRWFe; ndut_fmt=17DAF2FD0DC6DF723D10EB645D49FD8581EFDCCB4A2823D11359EA0CCE270FBE")
