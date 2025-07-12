from email.message import EmailMessage
import smtplib

# Einige SMTP Server
# ------------------
# mail.gmx.net
# posteo.de
# securesmtp.t-online.de
# smtp.gmail.com
# smtp.ionos.de (smtp.1und1.de)
# smtp.web.de
#
smtp_host = 'smtp_host'
smtp_user = 'smtp_user_name'
smtp_password = 'smtp_user_password'
#
# use TLS
use_tls = True
smtp_port = 465
#
# use STARTTLS
# use_tls = False
# smtp_port = 587
#
from_name = 'sender_name'
from_email = 'sender_email'
#
to_name = 'receiver_name'
to_email = 'receiver_mail'
#
subject = 'Subject: Test'
message = 'short_message_text'

try:
    msg = EmailMessage()
    msg['From'] = f'{from_name} <{from_email}>'
    msg['To'] = f'{to_name} <{to_email}>'
    msg['Subject'] = subject
    msg.set_content(message)

    if use_tls:
       smtp = smtplib.SMTP_SSL(host=smtp_host, port=smtp_port)
    else:
        smtp = smtplib.SMTP(host=smtp_host, port=smtp_port)
        # init STARTTLS
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

    smtp.login(smtp_user, smtp_password)
    smtp.send_message(msg)
    smtp.quit()
except smtplib.SMTPException as ex:
    print('SmtpMailer:', ex)
