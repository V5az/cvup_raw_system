
import os
import json
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

_sheet = None

def _get_sheet():
    global _sheet
    if _sheet is not None:
        return _sheet

    creds_json = os.getenv("GOOGLE_CREDS_JSON")
    if not creds_json:
        raise RuntimeError("Environment variable GOOGLE_CREDS_JSON is not set")

    creds_info = json.loads(creds_json)
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_info(creds_info, scopes=scopes)
    service = build("sheets", "v4", credentials=creds)
    _sheet = service.spreadsheets()
    return _sheet

def write_row(range_name: str, row: list):
    spreadsheet_id = os.getenv("SPREADSHEET_ID")
    if not spreadsheet_id:
        raise RuntimeError("Environment variable SPREADSHEET_ID is not set")

    sheet = _get_sheet()
    body = {"values": [row]}
    sheet.values().append(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption="RAW",
        body=body,
    ).execute()
