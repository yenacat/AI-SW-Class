import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="rabbit", password="AI000000", database="test"
)

mycursor = mydb.cursor(dictionary=True)

# ---------------------------------------------------------

# mycursor.execute("SELECT * FROM user")

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# ---------------------------------------------------------

# sql = "SELECT * FROM user WHERE NAME = 'Yena'"

# mycursor.execute(sql)
# myresult = mycursor.fetchone()

# print(myresult["NAME"], myresult["AGE"])

# ---------------------------------------------------------

# sql = "SELECT * FROM user WHERE AGE = %s"
# val = (21,)

# mycursor.execute(sql, val)
# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# ---------------------------------------------------------

# sql = "SELECT * FROM user ORDER BY AGE DESC"

# mycursor.execute(sql)
# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# ---------------------------------------------------------

sql = "DELETE FROM user WHERE NAME = %s"
val = ("Jihye",)

mycursor.execute(sql, val)
myresult = mycursor.fetchall()

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
