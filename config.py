from os import environ


# BOT CONFIG
API_ID = environ.get("API_ID", 123456)  # api id
API_HASH = environ.get("API_HASH", "")  # api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "")  # bot token

# REDIS
REDIS_HOST = environ.get("REDIS_HOST", "localhost")  # redis host uri
REDIS_PORT = environ.get("REDIS_PORT", 12345)  # redis port
REDIS_PASSWORD = environ.get(
    "REDIS_PASSWORD", "q8vcRgGfoZgwKT6irvJ6AixPs1lFZdW8"
)  # redis password


ADMINS = [6791744215]
OWNER_ID = 6791744215  # Replace with your Telegram user ID
PRIVATE_CHAT_ID = -100  # CHAT WHERE YOU WANT TO STORE VIDEOS
USER_CHANNEL = -100
DUMP_CHANNEL = -100


# Config
COOKIE = environ.get("COOKIE", "csrfToken=BnQx-ffuJKamkWLrsx3Ksds4; browserid=qEGrcJcpudjTVSp34yywiOK8KGczvjGYTPI6jJMydd7dpoQVUXCzDlp7JFM=; lang=en; __bid_n=18db31bdad1e0ee8094207; __stripe_mid=a300821a-4b38-4e0a-a227-5c27f1b7c54789f06e; __stripe_sid=f7b244b5-18a8-4540-bfa0-222b4acc0bf5eb56ba; ndus=Yb47bKTteHuiwDuAJYscQHtlthgbg2-2R4yRRWFe; ndut_fmt=17DAF2FD0DC6DF723D10EB645D49FD8581EFDCCB4A2823D11359EA0CCE270FBE")
