import mysql.connector

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['MYSQL_DATABASE_USER'] = 'asset'
app.config['MYSQL_DATABASE_PASSWORD'] = 'QveT@iei+1'
app.config['MYSQL_DATABASE_DB'] = 'asset'
app.config['MYSQL_DATABASE_HOST'] = '192.168.2.14'
app.config['MYSQL_DATABASE_PORT'] = '3307'

mysql = MySQL(app)


class DBManager:
    def __init__(self, user, password, host, database, port):
        self.mysql_connection = mysql.connector.connect(
            user=user, password=password, host=host, database=database, port=port)
        self.cursor = self.mysql_connection.cursor()

    def show_data(self, table_name):
        self.cursor.execute("Select * From {table_name}")
        values = self.cursor.fetchall()
        for asset in values:
            print(asset)


db_manager = DBManager(
    'asset', 'QveT@iei+1', '192.168.2.14', 'asset', '3307')

# db_manager.show_data('mAsset')


@app.route('/')
def test():
    return 'hello Mark'


@app.route('/device', methods=['POST'])
def postInput():
    insertValues = request.get_json()
    tableName = insertValues['test1']

    input = db_manager.show_data(tableName)

    # print(input)
    return input


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
