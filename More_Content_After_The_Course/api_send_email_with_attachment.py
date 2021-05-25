import smtplib
from email.message import EmailMessage
import imghdr
email_sender = "jka83321@gmail.com"
email_sender_password = "pvhjuhlojtqtocec"
message = EmailMessage()
message["Subject"] = "See Attachment"
message["From"] = email_sender
message["To"] = "jka83321@gmail.com"
message.set_content("See image below")
with open("python-logo.png","rb") as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name
message.add_attachment(file_data,maintype="image",subtype=file_type,filename=file_name)
with smtplib.SMTP_SSL("smtp.gmail.com",465) as smpt:
    smpt.login(email_sender,email_sender_password)
    smpt.send_message(message)