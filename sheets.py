# sheets.py
from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

# Load credentials and initialize Google Sheets API
SERVICE_ACCOUNT_FILE = 'D:\SuperJoin\superjoin-435715-64f0c30e6e9f.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)

SHEET_ID = 'superjoin'
RANGE_NAME = 'Sheet1!A:C'

def read_sheet():
    sheet = service.spreadsheets().values().get(spreadsheetId=SHEET_ID, range=RANGE_NAME).execute()
    values = sheet.get('values', [])
    keys = ['column1', 'column2', 'column3']
    return [dict(zip(keys, row)) for row in values]

def write_sheet(data):
    body = {'values': data}
    service.spreadsheets().values().update(spreadsheetId=SHEET_ID, range=RANGE_NAME, valueInputOption='RAW', body=body).execute()
