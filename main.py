import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

from important_user import ImportantUser
from user import User
import config
import os

if __name__ == "__main__":
    '''
    Calling User object and send_plain_mail method will result in sending text html message to the email via SMTP.
    Calling ImportantUser object and send_mail_with_attachment method will result in sending text html, signature logo and attachment mail via SMTP.
    '''
    user = User(config.sender, config.password, config.smtp_name, config.smtp_port)
    user.send_plain_mail(config.receiver, config.subject, config.body)
    important_user = ImportantUser(config.sender, config.password, config.smtp_name, config.smtp_port,
                                   config.signature_img_name, config.signature_img_path, config.attachment_name,
                                   config.attachment_path)
    important_user.send_mail_with_attachment(config.receiver, config.subject, config.important_body)
