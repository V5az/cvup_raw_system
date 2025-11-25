
import hashlib
import datetime
from telethon import TelegramClient, events
from shared.shared_write import write_row
import os

# Telegram credentials from environment
api_id = int(os.getenv("TG_API_ID", "0"))
api_hash = os.getenv("TG_API_HASH", "")

if not api_id or not api_hash:
    raise RuntimeError("TG_API_ID or TG_API_HASH not set in environment")

CHANNELS = [
    "https://t.me/ewdifh",
    "https://t.me/Engineers_Jobs",
    "https://t.me/grobksa",
]

client = TelegramClient("cvup_telegram_session", api_id, api_hash)

def _get_hash(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()

async def run_telegram_scraper():
    print("🔵 Telegram scraper started...")

    @client.on(events.NewMessage(chats=CHANNELS))
    async def handler(event):
        msg = event.message.message or ""
        if not msg.strip():
            return

        hash_value = _get_hash(msg)
        now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        channel_name = event.chat.title if event.chat else "Unknown"

        row = [
            str(event.message.id),
            msg,
            channel_name,
            now,
            hash_value,
        ]

        # الكتابة في تبويب jobs_telegram_raw
        write_row("jobs_telegram_raw!A:E", row)

        print(f"✔ New Telegram job saved from: {channel_name}")

    await client.start()
    await client.run_until_disconnected()
