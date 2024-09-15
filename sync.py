# sync.py
import time
from sheets import read_sheet
from db import read_db, insert_db, update_db, delete_db

def sync_google_sheets_to_db():
    sheet_data = read_sheet()
    db_data = read_db()

    # Convert sheet data to a set of tuples for comparison
    sheet_data_set = set(tuple(record.values()) for record in sheet_data)
    
    # Convert database data to a set of tuples for comparison
    db_data_set = set(tuple(record.values()) for record in db_data)

    # Insert records from Google Sheets that are not in the database
    for row in sheet_data:
        record = (row.get('column1', ''), row.get('column2', ''), row.get('column3', ''))
        if record not in db_data_set:
            insert_db(*record)
            print(f"Inserted record {record}")

    # Optional: Sync database to Google Sheets
    # sync_db_to_google_sheets()

def sync_db_to_google_sheets():
    db_data = read_db()
    sheet_data = [[row['column1'], row['column2'], row['column3']] for row in db_data]
    write_sheet(sheet_data)

def main():
    # Polling interval in seconds
    polling_interval = 60

    print("Starting synchronization...")

    while True:
        sync_google_sheets_to_db()
        # Optional: Uncomment the following line if you want to sync DB to Sheets as well
        # sync_db_to_google_sheets()
        time.sleep(polling_interval)

if __name__ == "__main__":
    main()
