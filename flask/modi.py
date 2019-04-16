#!/usr/bin/env python
from flask import Flask, jsonify, request
app = Flask(__name__)

import mysql.connector
from mysql.connector import Error
import threading
import time

conn = mysql.connector.connect(database = "epics", user = "Rishabh", password = "chitkara", host = "epics.cchqlmtm8iyr.us-east-1.rds.amazonaws.com", port = "3306")
print ('Opened database successfully')
cur = conn.cursor()

        



# @app.route('/', methods=['GET'])
# def test():
#     return jsonify({'message': 'It works'})

@app.route('/', methods=['GET'])
def ow():
    global cur
    cur.execute("SELECT * from studentDetails")
    rows = cur.fetchall()
    data = []
    for row in rows:
        print(row)
        roll = str(row[0])
        name = str(row[1])
        attended = str(row[2])
        data += [{'roll':roll,'name':name,'attended':attended}]
    return jsonify(data)
dt = []


if __name__ == '__main__':
    app.run(debug=True)
    
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port="80")




