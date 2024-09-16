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

    print(f"Resolving conflict for ID {sheet_row['id']}:")
    print(f"Sheet Time: {sheet_time}, DB Time: {db_time}")

    # Compare times and resolve conflicts
    if sheet_time > db_time:
        print("Sheet has newer data.")
        return sheet_row
    elif sheet_time < db_time:
        print("DB has newer data.")
        return db_row
    else:
        # If times are the same, compare the actual data
        if (sheet_row['column1'] != db_row['column1'] or
            sheet_row['column2'] != db_row['column2'] or
            sheet_row['column3'] != db_row['column3']):
            print("Data differs despite identical timestamps. Updating DB with sheet data.")
            return sheet_row
        else:
            print("Data is identical.")
            return db_row

# Synchronize data from Google Sheets to MySQL
def sync_google_sheets_to_db():
    try:
        sheet_data = read_sheet()
        db_data = read_db()

        db_data_dict = {row['id']: row for row in db_data}

        for row in sheet_data:
            row_id = row.get('id', None)
            if not row_id:
                print(f"Skipping row with missing ID: {row}")
                continue

            if row_id in db_data_dict:
                resolved_row = resolve_conflict(row, db_data_dict[row_id])
                if (resolved_row['column1'] != db_data_dict[row_id]['column1'] or
                    resolved_row['column2'] != db_data_dict[row_id]['column2'] or
                    resolved_row['column3'] != db_data_dict[row_id]['column3']):
                    print(f"Updating DB with: {resolved_row}")
                    update_db(resolved_row['column1'], resolved_row['column2'], resolved_row['column3'], row_id)
            else:
                print(f"Inserting into DB: {row}")
                insert_db(row_id, row.get('column1', ''), row.get('column2', ''), row.get('column3', ''))

        db_ids = set(db_data_dict.keys())
        sheet_ids = set(row.get('id') for row in sheet_data)
        rows_to_delete = db_ids - sheet_ids

        for row_id in rows_to_delete:
            print(f"Deleting from DB: {row_id}")
            delete_db(row_id)

    except Exception as e:
        print(f"Error during Sheets to DB sync: {e}")

# Synchronize data from MySQL to Google Sheets
def sync_db_to_google_sheets():
    try:
        db_data = read_db()

        # Convert datetime objects to string for JSON serialization
        formatted_db_data = []
        for row in db_data:
            formatted_row = row.copy()
            if isinstance(formatted_row['last_updated'], datetime):
                formatted_row['last_updated'] = formatted_row['last_updated'].strftime('%Y-%m-%d %H:%M:%S')
            formatted_db_data.append(formatted_row)

        # Prepare new sheet data
        new_sheet_data = [['id', 'column1', 'column2', 'column3', 'last_updated']]
        new_sheet_data.extend([[row['id'], row['column1'], row['column2'], row['column3'], row['last_updated']] for row in formatted_db_data])
        
        # Write new data to Google Sheets
        write_sheet(new_sheet_data)

        # Handle deletions in Google Sheets
        sheet_data = read_sheet()
        sheet_ids = {row['id'] for row in sheet_data}
        db_ids = {row['id'] for row in formatted_db_data}
        rows_to_delete = sheet_ids - db_ids

        if rows_to_delete:
            for row_id in rows_to_delete:
                for idx, row in enumerate(sheet_data):
                    if row['id'] == row_id:
                        delete_from_sheet(idx + 2)  # Adjust for 1-based indexing in Sheets

    except Exception as e:
        print(f"Error during DB to Sheets sync: {e}")

# Polling to detect changes
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
        time.sleep(15)  # Adjust the sleep interval as needed

if __name__ == "__main__":
    main()
