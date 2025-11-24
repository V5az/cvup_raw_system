from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import datetime
import json

# ===== إعدادات Google Sheets =====
SERVICE_ACCOUNT_FILE = "arched-memory-465912-s8-186402f6fe5b.json"

# حط هنا نفس الـ Spreadsheet ID حق ملف CVUP_RAW_SYSTEM
SPREADSHEET_ID = "1ik_zphtgwLK-K069jhHgW5KJgwvLH31MbcmAtguKnXs"

# اسم الورقة اللي سويتها للجدارات
RANGE_NAME = "jobs_jadarat_raw!A:H"

# تجهيز الاتصال بجوجل شيت
creds = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=["https://www.googleapis.com/auth/spreadsheets"],
)
sheets_service = build("sheets", "v4", credentials=creds)
sheet = sheets_service.spreadsheets()


async def run_jadarat_scraper():
    print("🔥 Jadarat RAW scraper started (test mode)")

    # هنا بس نرسل وظيفة تجريبية عشان نتأكد إن كل شي شغال
    job = {
        "job_id": "TEST-123",
        "title": "Test Job from Jadarat (RAW)",
        "company": "Test Company",
        "city": "Riyadh",
        "description": "This is a test row from the server (Jadarat RAW).",
        "link": "https://jadarat.sa/",
        "raw_json": {"source": "manual_test"},
    }

    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    row = [
        now,
        job["job_id"],
        job["title"],
        job["company"],
        job["city"],
        job["description"],
        job["link"],
        json.dumps(job["raw_json"], ensure_ascii=False),
    ]

    sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption="RAW",
        body={"values": [row]},
    ).execute()

    print("✔ Test row pushed to Google Sheets in jobs_jadarat_raw")
