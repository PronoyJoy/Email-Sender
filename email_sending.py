
from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'jkdas242@gmail.com'
email_password = ''

email_receiver ='sicame2641@ekbasia.com'

subject = 'Hello Buddy'

body = """
You will be a star
"""

em = EmailMessage()

em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())