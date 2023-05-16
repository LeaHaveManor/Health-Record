import mysql.connector

try:
    db = mysql.connector.connect(
        user='root',
        password='Banan123',
        host='127.0.0.1',
        database='mydb'
    )
    print("connected")

except Exception as e:
    print(e)

#Class Patient
### Connect til database






