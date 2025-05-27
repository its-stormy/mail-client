import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# Email credentials and config
SMTP_SERVER = 'mail.examplemail.com'  # Replace with your SMTP server (e.g., mail.privateemail.com)
SMTP_PORT = 587
SENDER_EMAIL = 'user@example.com'     # Your full email address
RECIPIENT_EMAIL = 'recipient@example.com'
EMAIL_SUBJECT = 'Test Email Subject'

# Read password from a file
with open("password.txt", 'r') as f:
    EMAIL_PASSWORD = f.read().strip()

# Setup the SMTP connection
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.ehlo()
server.starttls()
server.ehlo()
server.login(SENDER_EMAIL, EMAIL_PASSWORD)

# Create the email
msg = MIMEMultipart()
msg['From'] = f'User <{SENDER_EMAIL}>'
msg['To'] = RECIPIENT_EMAIL
msg['Subject'] = EMAIL_SUBJECT

# Attach the email body (plain text)
with open('message.txt', 'r') as f:
    message = f.read()
msg.attach(MIMEText(message, 'plain'))

# Attach a file (e.g., image or document)
filename = 'attachment.png'  # Replace with your file
with open(filename, 'rb') as attachment:
    mime_base = MIMEBase('application', 'octet-stream')
    mime_base.set_payload(attachment.read())
    encoders.encode_base64(mime_base)
    mime_base.add_header('Content-Disposition', f'attachment; filename={filename}')
    msg.attach(mime_base)

# Send the email
server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
server.quit()
