import smtplib
from email.mime.text import MIMEText

print("Starting SMTP test script...")  # Debugging line

# SMTP Server Configuration
smtp_server = "smtp.gmail.com"
port = 587  # TLS
sender_email = "baltimore273@gmail.com"
app_password = "slxv ewjq tkig fqkf"  # 
recipient_email = "theeville712@gmail.com"

# Create the email
message = MIMEText("This is a test email sent using Gmail's SMTP server.")
message['Subject'] = "SMTP Test Email"
message['From'] = sender_email
message['To'] = recipient_email

try:
    print("Connecting to SMTP server...")  # Debugging line
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()  # Secure the connection
        print("Logging in...")  # Debugging line
        server.login(sender_email, app_password)  # Login
        print("Sending email...")  # Debugging line
        server.sendmail(sender_email, recipient_email, message.as_string())  # Send email
        print("Email sent successfully!")  # Debugging line
except Exception as e:
    print(f"An error occurred: {e}")



