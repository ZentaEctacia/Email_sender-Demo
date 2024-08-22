import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = "zentaectacia@gmail.com"
receiver_email ="saba.nazir.2210@gmail.com"
password = "fkay jmaj ivfy vfyo"  # Or app password if 2FA is enabled
subject = "testing"
body = "Hi this is the checking mail."

# Create the MIME message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    # Set up the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        smtp.login(sender_email, password)

        # Send the email
        text = msg.as_string()
        smtp.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully!")

except Exception as e:
    print(f"Failed to send email: {e}")
