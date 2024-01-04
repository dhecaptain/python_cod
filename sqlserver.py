
# Import the necessary modules.
import mysql.connector
import hashlib

# Create a connection to the database.
connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="user_login_registration"
)

# Create a cursor object.
cursor = connection.cursor()

# Create a function to register a new user.
def register_user(username, password):
  # Hash the password.
  hashed_password = hashlib.sha256(password.encode()).hexdigest()

  # Create a new user in the database.
  cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))

  # Commit the changes to the database.
  connection.commit()

# Create a function to login a user.
def login_user(username, password):
  # Hash the password.
  hashed_password = hashlib.sha256(password.encode()).hexdigest()

  # Check if the user exists in the database.
  cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, hashed_password))

  # Get the user's data.
  user = cursor.fetchone()

  # If the user exists, return the user's data.
  if user:
    return user

  # If the user does not exist, return None.
  else:
    return None

# Close the cursor object.
cursor.close()

# Close the connection to the database.
connection.close()