from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api

# Create an instance of Flask
app = Flask(__name__)

# Create an instance of MySQL
mysql = MySQL()

# Create an instance of Flask RESTful API
api = Api(app)

# Set database credentials in config.
app.config['MYSQL_DATABASE_USER'] = 'asset'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Qvi+1'
app.config['MYSQL_DATABASE_DB'] = 'asset'
app.config['MYSQL_DATABASE_HOST'] = '192.1.1'
app.config['MYSQL_DATABASE_PORT'] = 3306

# Initialize the MySQL extension
mysql.init_app(app)


# Get All Users, or Create a new user
class UserList(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""Select * From mAsset""")
            rows = cursor.fetchall()
            # print(rows)
            return jsonify(rows)
        except Exception as e:
            print(e)
            return e
        # finally:
        #     cursor.close()
        #     conn.close()


# Get a user by id, update or delete user

# API resource routes
api.add_resource(UserList, '/ddde')
# api.add_resource(User, '/user/<int:user_id>', endpoint='user')

if __name__ == "__main__":
    app.run(debug=True)
