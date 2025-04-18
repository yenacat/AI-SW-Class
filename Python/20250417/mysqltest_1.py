import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="rabbit", password="AI000000", database="test"
)

mycursor = mydb.cursor()

sql = "INSERT INTO user (NAME, AGE) VALUES (%s, %s)"
val = ("Yena", 21)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
