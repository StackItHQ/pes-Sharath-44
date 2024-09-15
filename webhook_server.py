# webhook_server.py
from flask import Flask, request, jsonify
from sheets import read_sheet, write_sheet
from db import read_db, insert_db, update_db, delete_db

app = Flask(__name__)

@app.route('/sync', methods=['POST'])
def sync_data():
    data = request.json
    if not data:
        return jsonify({'status': 'error', 'message': 'No data provided'}), 400

    if 'action' in data:
        action = data['action']
        records = data.get('records', [])

        if action == 'insert':
            for record in records:
                column1 = record.get('column1', '')
                column2 = record.get('column2', '')
                column3 = record.get('column3', '')
                insert_db(column1, column2, column3)
            return jsonify({'status': 'success', 'message': 'Data inserted successfully'}), 200

        elif action == 'update':
            for record in records:
                id = record.get('id')
                column1 = record.get('column1', '')
                column2 = record.get('column2', '')
                column3 = record.get('column3', '')
                update_db(id, column1, column2, column3)
            return jsonify({'status': 'success', 'message': 'Data updated successfully'}), 200

        elif action == 'delete':
            ids = data.get('ids', [])
            for id in ids:
                delete_db(id)
            return jsonify({'status': 'success', 'message': 'Data deleted successfully'}), 200

    return jsonify({'status': 'error', 'message': 'Invalid action'}), 400

if __name__ == "__main__":
    app.run(port=5000)
