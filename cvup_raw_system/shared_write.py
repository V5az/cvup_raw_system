
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# ملف الخدمة من Google - يجب أن تضع الملف الحقيقي في نفس المجلد
SERVICE_ACCOUNT_FILE = "arched-memory-465912-s8-186402f6fe5b.json"

# ID ملف Google Sheets
SPREADSHEET_ID = "1ik_zphtgwLK-K069jhHgW5KJgwvLH31MbcmAtguKnXs"

# تهيئة الاتصال مرة واحدة فقط
_SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
_creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=_SCOPES)
_service = build("sheets", "v4", credentials=_creds)
_sheet = _service.spreadsheets()


def write_row(range_name: str, row: list):
    """كتابة صف واحد في Google Sheets."""
    body = {"values": [row]}
    _sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=range_name,
        valueInputOption="RAW",
        body=body,
    ).execute()
