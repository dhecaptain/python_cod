import smtplib

# Set up the SMTP server
smtp_server = "smtp.gmail.com"
port = 587  # For TLS
username = "davidpolycarp7@gmail.com"
password = "david1234"

# Create a secure connection
server = smtplib.SMTP(smtp_server, port)
server.starttls()

# Login to the SMTP server
server.login(username, password)

# Send the email
msg = "how you bro, send the money that I lent to you."
server.sendmail(username, "davidpolycarp298@gmail.com", msg)

# Quit the SMTP server
server.quit()
