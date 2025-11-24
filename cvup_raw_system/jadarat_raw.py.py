from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import requests
import datetime

# ===== Google Sheets =====
SERVICE_ACCOUNT_FILE = "arched-memory-465912-s8-186402f6fe5b.json"
SPREADSHEET_ID = "1ik_zphtgwLK-K069jhHgW5KJgwvLH31MbcmAtguKnXs"
RANGE_NAME = "Jobs!A:E"

creds = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)
sheets_service = build("sheets", "v4", credentials=creds)
sheet = sheets_service.spreadsheets()

# ===== simple jadarat test (placeholder) =====
def fetch_jadarat_fake():
    return [
        "Test Job from Jadarat (RAW MODE)",
        "https://jadarat.sa/JobDetails/TestID"
    ]

def save_to_sheet(data):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [now, data[0], data[1], "jadarat_raw", ""]
    sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption="RAW",
        body={"values": [row]}
    ).execute()
    print("✔ Saved Row:", row)

print("🔥 RAW jadarat collector running...")
jobs = fetch_jadarat_fake()
save_to_sheet(jobs)