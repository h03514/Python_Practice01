import pymysql

dbhost = 'localhost'
dbuser = 'aeewt'
dbpass = 'Qi+'
dbname = 'asset'

db = pymysql.connect(host=dbhost, user=dbuser,
                     password=dbpass, database=dbname)
cursor = db.cursor()

sql = 'SELECT * FROM masset'

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        #print (row)
        sn = row[0]
        assetnum = row[1]
        brand = row[2]
        decivetype = row[3]
        model = row[4]
        # Now print fetched result
        print("sn = %s, assetnum= %s ,brand = %s ,decivetype = %s ,model = %s" %
              (sn, assetnum, brand, decivetype, model))
except:
    import traceback
    traceback.print_exc()

    print("Error: unable to fetch data")

# disconnect from server
db.close()
