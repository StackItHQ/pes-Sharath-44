from sheets import read_sheet, write_sheet, update_sheet, delete_from_sheet
from db import read_db, insert_db, update_db, delete_db
import time

last_sync_time = time.time()

# Synchronize data from Google Sheets to MySQL
def sync_google_sheets_to_db():
    sheet_data = read_sheet()
    print("Sheet Data: ", sheet_data)  # Debugging line to print fetched sheet data
    for row in sheet_data:
        row_id = row.get('id', None)  # Ensure 'id' is part of your Google Sheets data
        if row_id:
            update_db(row.get('column1', ''), row.get('column2', ''), row.get('column3', ''), row_id)
        else:
            insert_db(row.get('column1', ''), row.get('column2', ''), row.get('column3', ''))


# Synchronize data from MySQL to Google Sheets
def sync_db_to_google_sheets():
    try:
        db_data = read_db()
        print("DB Data: ", db_data)  # Debugging line
        sheet_data = [['id', 'column1', 'column2', 'column3']]
        sheet_data.extend([[row['id'], row['column1'], row['column2'], row['column3']] for row in db_data])
        write_sheet(sheet_data)
    except Exception as e:
        print(f"Error during DB to Sheets sync: {e}")


# Polling to detect changes (basic example)
def poll_google_sheets():
    global last_sync_time
    # Implement change detection logic here
    last_sync_time = time.time()  # Update last_sync_time after processing

def poll_db():
    global last_sync_time
    # Implement change detection logic here
    last_sync_time = time.time()  # Update last_sync_time after processing

def main():
    global last_sync_time
    last_sync_time = time.time()
    while True:
        poll_google_sheets()
        poll_db()
        sync_google_sheets_to_db()
        sync_db_to_google_sheets()
        time.sleep(15)  # Adjust the sleep interval based on requirements

if __name__ == "__main__":
    main()
