
import hashlib
import datetime
from telethon import TelegramClient, events
from shared_write import write_row

# ===== إعدادات Telegram =====
api_id = 35479481
api_hash = "8f12ca035cdad9e39e471b6ae2e2dd25"

# القنوات التي سيتم سحب الوظائف منها
CHANNELS = [
    "https://t.me/ewdifh",
    "https://t.me/Engineers_Jobs",
    "https://t.me/grobksa",
]

# اسم جلسة التليجرام (سيتم إنشاء ملف session تلقائياً في نفس المجلد على السيرفر)
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

        # الكتابة في الشيت في تبويب Jobs الأعمدة A:E
        write_row("Jobs!A:E", row)

        print(f"✔ New Telegram job saved from: {channel_name}")

    await client.start()
    await client.run_until_disconnected()
