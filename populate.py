import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="{password}",
database="Flight_Management"
)
cursor = mydb.cursor()
query="INSERT INTO ADMINISTRATOR (Name,CNIC,Phone_no) VALUES (%s,%s,%s)"
admin=("sam","3310045023879","03326661247")
cursor.execute(query,admin)
recep=("sam","3310121123412","03326671247")
query="INSERT INTO RECEPTIONIST (Name,CNIC,Phone_no) VALUES (%s,%s,%s)"
cursor.execute(query,recep)
mydb.commit()

    
