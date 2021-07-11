from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'dd'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Qd+1'
app.config['MYSQL_DATABASE_DB'] = 'asset'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
