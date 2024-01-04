import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#David2015",
  database="student"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE tasks (id INT PRIMARY KEY, description VARCHAR(255), completed BOOLEAN)")

mycursor.execute("INSERT INTO tasks (id, description, completed) VALUES (1, 'Task 1', False)")

mycursor.execute("SELECT * FROM tasks")

for x in mycursor:
  print(x)
