from telethon import TelegramClient, events
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import datetime, hashlib

SERVICE_ACCOUNT_FILE = "arched-memory-465912-s8-186402f6fe5b.json"
SPREADSHEET_ID = "1ik_zphtgwLK-K069jhHgW5KJgwvLH31MbcmAtguKnXs"
RANGE_NAME = "telegram_raw!A:E"

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scopes)
sheet = build('sheets', 'v4', credentials=creds).spreadsheets()

api_id = 35479481
api_hash = "8f12ca035cdad9e39e471b6ae2e2dd25"

CHANNELS = [
    "ewdifh",
    "Engineers_Jobs",
    "grobksa"
]

client = TelegramClient('cvup_session', api_id, api_hash)

def get_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

async def run_telegram_scraper():
    @client.on(events.NewMessage(chats=CHANNELS))
    async def handler(event):
        msg = event.message.message.strip()
        if not msg:
            return

        row = [
            str(event.message.id),
            msg,
            event.chat.title,
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            get_hash(msg)
        ]

        sheet.values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME,
            valueInputOption="RAW",
            body={"values": [row]}
        ).execute()

        print("✔ NEW TELEGRAM MESSAGE SAVED")

    await client.start()
    await client.run_until_disconnected()
