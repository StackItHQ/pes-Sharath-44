# sync.py
from sheets import read_sheet, write_sheet
from db import read_db, insert_db

# Synchronize data from Google Sheets to MySQL
def sync_google_sheets_to_db():
    sheet_data = read_sheet()
    for row in sheet_data:
        insert_db(row.get('column1', ''), row.get('column2', ''), row.get('column3', ''))

# Synchronize data from MySQL to Google Sheets
def sync_db_to_google_sheets():
    db_data = read_db()
    # Convert database data to the format expected by Google Sheets
    sheet_data = [[row['column1'], row['column2'], row['column3']] for row in db_data]
    write_sheet(sheet_data)

def main():
    sync_google_sheets_to_db()
    sync_db_to_google_sheets()

if __name__ == "__main__":
    main()
