import smtplib

sender_mail = 'davidpolycarp7@gmail.com'
receiver_mail = ['davidpolycarp298@gmail.com']
subject = 'Sending SMTP e-mail'

message = f"""\
From: {sender_mail}
To: {', '.join(receiver_mail)}
Subject: {subject}

This is the last message.
"""

try:
    smtpObj = smtplib.SMTP('smtp.your-email-provider.com', 587)  # Update with your SMTP server and port
    smtpObj.starttls()
    smtpObj.login('your_username', 'your_password')  # Update with your email credentials
    smtpObj.sendmail(sender_mail, receiver_mail, message)
    print('Successfully sent email')
    smtpObj.quit()
except Exception as e:
    print(f'ERROR: Unable to send email - {e}')
