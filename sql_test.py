import mysql.connector
from mysql.connector import Error


mysql_connection = mysql.connector.connect(
    host='192.168.45.14',
    user="asset",
    password="Qvpei+1",
    port='3306',
    charset='utf8',
    database="asset"
)

cursor = mysql_connection.cursor()
cursor.execute("SELECT * FROM `mAsset`")
asset = cursor.fetchall()
for i in asset:
    print(i)
mysql_connection.close()
# 使用 cursor() 方法建立一個遊標物件cursor
# cursor = db.cursor()
# # SQL語句
# sql = "SELECT * FROM `mAsset` WHERE sn= 'B5PFAG000786'"
# try:
#     cursor.execute(sql)
#     results = cursor.fetchall()  # 獲取全部結果集。  fetchone 查詢第一條資料
#     if not results:  # 判斷是否為空。
#         print("資料為空！")
#     else:
#         print(results)
# except Exception as e:
#     db.rollback()  # 如果出錯就會滾資料庫並且輸出錯誤資訊。
#     print("Error:{0}".format(e))
# finally:
#     db.close()  # 關閉資料庫。
