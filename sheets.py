# sheets.py
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Authenticate using the service account key
creds = ServiceAccountCredentials.from_json_keyfile_name('D:\SuperJoin\superjoin-435715-64f0c30e6e9f.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open('superjoin').sheet1

# Read data from Google Sheets
def read_sheet():
    return sheet.get_all_records()

# Write data to Google Sheets
def write_sheet(values):
    sheet.update('A1', values)
