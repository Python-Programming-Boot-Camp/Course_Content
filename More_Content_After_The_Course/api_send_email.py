import smtplib
email_sender = "jka83321@gmail.com"
email_sender_password = "pvhjuhlojtqtocec"
with smtplib.SMTP_SSL("smtp.gmail.com",465) as smpt:
    smpt.login(email_sender,email_sender_password)
    subject = "Test"
    body = "How are you?"
    message = f"Subject:{subject}\n\n{body}"
    smpt.sendmail(email_sender,"jka83321@gmail.com",message)