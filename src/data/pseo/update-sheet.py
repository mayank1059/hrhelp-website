#!/usr/bin/env python3
"""Update Google Sheet with full pSEO schedule: live + planned pages."""
import json, os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
token_file = '/Users/mayanktewari/Vibe/amsterdamkids/token.json'
SPREADSHEET_ID = '1cnIu-Pk3-2LXaPmLVmkuePhDJDHD4CeRJzuOduw-jIE'

# Load rows
with open('/tmp/pseo_rows.json') as f:
    rows = json.load(f)

# Auth
creds = Credentials.from_authorized_user_file(token_file, SCOPES)
service = build('sheets', 'v4', credentials=creds)

# Rename sheet tab
try:
    sheet_metadata = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
    sheets = sheet_metadata.get('sheets', '')
    sheet_id = sheets[0].get("properties", {}).get("sheetId", 0)
    
    service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID,
        body={"requests": [{
            "updateSheetProperties": {
                "properties": {"sheetId": sheet_id, "title": "HRHELP PSEO SCHEDULE"},
                "fields": "title"
            }
        }]}
    ).execute()
    print("Renamed sheet tab.")
except Exception as e:
    print(f"Notice: {e}")

# Clear existing
try:
    service.spreadsheets().values().clear(
        spreadsheetId=SPREADSHEET_ID, range='A1:F200'
    ).execute()
except:
    pass

# Write data
result = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID, range='A1',
    valueInputOption='RAW', body={'values': rows}
).execute()

print(f"✅ Updated {result.get('updatedCells')} cells ({len(rows)-1} pages)")

# Format: bold header, color live rows green, planned rows blue
requests = []

# Bold header
requests.append({
    "repeatCell": {
        "range": {"sheetId": sheet_id, "startRowIndex": 0, "endRowIndex": 1},
        "cell": {"userEnteredFormat": {
            "textFormat": {"bold": True},
            "backgroundColor": {"red": 0.12, "green": 0.16, "blue": 0.38}
        }},
        "fields": "userEnteredFormat(textFormat,backgroundColor)"
    }
})

# Header text color white
requests.append({
    "repeatCell": {
        "range": {"sheetId": sheet_id, "startRowIndex": 0, "endRowIndex": 1},
        "cell": {"userEnteredFormat": {"textFormat": {"bold": True, "foregroundColor": {"red": 1, "green": 1, "blue": 1}}}},
        "fields": "userEnteredFormat.textFormat"
    }
})

# Count live vs planned
live_count = sum(1 for r in rows[1:] if 'Live' in str(r[5]))
planned_start = 1 + live_count

# Green background for live rows
requests.append({
    "repeatCell": {
        "range": {"sheetId": sheet_id, "startRowIndex": 1, "endRowIndex": planned_start},
        "cell": {"userEnteredFormat": {"backgroundColor": {"red": 0.85, "green": 0.95, "blue": 0.85}}},
        "fields": "userEnteredFormat.backgroundColor"
    }
})

# Light blue background for planned rows
requests.append({
    "repeatCell": {
        "range": {"sheetId": sheet_id, "startRowIndex": planned_start, "endRowIndex": len(rows)},
        "cell": {"userEnteredFormat": {"backgroundColor": {"red": 0.86, "green": 0.92, "blue": 1.0}}},
        "fields": "userEnteredFormat.backgroundColor"
    }
})

# Auto-resize columns
requests.append({
    "autoResizeDimensions": {
        "dimensions": {"sheetId": sheet_id, "dimension": "COLUMNS", "startIndex": 0, "endIndex": 6}
    }
})

service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID,
    body={"requests": requests}
).execute()

print("✅ Formatting applied (header, live=green, planned=blue)")
