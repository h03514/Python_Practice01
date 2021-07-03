import mysql.connector


class DBManager:
    def __init__(self, user, password, host, database, port):
        self.mysql_connection = mysql.connector.connect(
            user=user, password=password, host=host, database=database, port=port)
        self.cursor = self.mysql_connection.cursor()

    def show_data(self, table_name):
        self.cursor.execute(f"Select * From {table_name}")
        values = self.cursor.fetchall()
        for asset in values:
            print(asset)


db_manager = DBManager('asset', 'Qveei+1', '192.168.25.14', 'aSLset', '3306')

# db_manager.show_data('mAsset')
