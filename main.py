import os
from flask import Flask, request, jsonify
# from utils.s3Functions import put_object, get_signed_url
import json

from dotenv import load_dotenv
from mysql.connector import Error
import mysql.connector
from datetime import datetime


load_dotenv()

# connection = MySQLdb.connect(
#     host=os.getenv("DB_HOST"),
#     user=os.getenv("DB_USERNAME"),
#     passwd=os.getenv("DB_PASSWORD"),
#     db=os.getenv("DB_NAME"),
#     autocommit=True,
#     ssl_mode="VERIFY_IDENTITY",
#     ssl={
#         "ca": "/etc/ssl/cert.pem"
#     }
# )

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    ssl_ca=os.getenv("SSL_CERT")
)


try:
    if connection.is_connected():
        cursor = connection.cursor()
    cursor.execute("select @@version ")
    version = cursor.fetchone()
    if version:
        print('Running version: ', version)
    else:
        print('Not connected.')
    # get all the tables
    # cursor.execute("select * from uploaded_files")
    # tables = cursor.fetchall()
    # print(tables)
except Error as e:
    print("Error while connecting to MySQL", e)


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
