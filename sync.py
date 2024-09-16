from sheets import read_sheet, write_sheet, update_sheet, delete_from_sheet
from db import read_db, insert_db, update_db, delete_db
import time
from datetime import datetime

last_sync_time = time.time()

# Conflict resolution function
def resolve_conflict(sheet_row, db_row):
    # Convert sheet_row last_updated to datetime for comparison
    sheet_time = datetime.strptime(sheet_row['last_updated'], '%Y-%m-%d %H:%M:%S')
    db_time = db_row['last_updated']
    
    # Ensure db_time is a datetime object
    if isinstance(db_time, str):
        db_time = datetime.strptime(db_time, '%Y-%m-%d %H:%M:%S')

    if sheet_time > db_time:
        return sheet_row
    return db_row

# Synchronize data from Google Sheets to MySQL
def sync_google_sheets_to_db():
    sheet_data = read_sheet()
    print("Sheet Data: ", sheet_data)  # Debugging line to print fetched sheet data
    db_data = read_db()
    print("DB Data: ", db_data)  # Debugging line to print fetched database data
    
    db_data_dict = {row['id']: row for row in db_data}
    
    for row in sheet_data:
        row_id = row.get('id', None)
        if row_id in db_data_dict:
            resolved_row = resolve_conflict(row, db_data_dict[row_id])
            if (resolved_row['column1'] != db_data_dict[row_id]['column1'] or
                resolved_row['column2'] != db_data_dict[row_id]['column2'] or
                resolved_row['column3'] != db_data_dict[row_id]['column3']):
                print(f"Updating DB with: {resolved_row}")  # Debugging line
                update_db(resolved_row['column1'], resolved_row['column2'], resolved_row['column3'], row_id)
        else:
            print(f"Inserting into DB: {row}")  # Debugging line
            insert_db(row.get('column1', ''), row.get('column2', ''), row.get('column3', ''))

    db_ids = set(db_data_dict.keys())
    sheet_ids = set(row.get('id') for row in sheet_data)
    rows_to_delete = db_ids - sheet_ids

    for row_id in rows_to_delete:
        print(f"Deleting from DB: {row_id}")  # Debugging line
        delete_db(row_id)

# Synchronize data from MySQL to Google Sheets
def sync_db_to_google_sheets():
    try:
        db_data = read_db()
        print("DB Data for Sheets: ", db_data)  # Debugging line
        sheet_data = read_sheet()

        new_sheet_data = [['id', 'column1', 'column2', 'column3']]
        new_sheet_data.extend([[row['id'], row['column1'], row['column2'], row['column3']] for row in db_data])
        write_sheet(new_sheet_data)

        db_ids = {row['id'] for row in db_data}
        sheet_ids = {row.get('id') for row in sheet_data}
        rows_to_delete = sheet_ids - db_ids

        for idx, row in enumerate(sheet_data):
            if row['id'] in rows_to_delete:
                print(f"Deleting from Sheets: {idx + 2}")  # Debugging line
                delete_from_sheet(idx + 2)  # Row index starts at 2 to skip the header

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
