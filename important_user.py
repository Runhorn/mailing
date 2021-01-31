import smtplib
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

from user import User
from mail import Mail


class ImportantUser(User):
    '''
    ImportantUser class inherits from User class. It is more complex version of it. It let's user add attachment to mail
    paired with signature image (ex. logo).
    Input:
    sender, password, smtp_name - str
    smtp_port - int
    attachment_name, signature_img_name - is a str name of a file with the extension
    attachment_path, signature_img_path - is a str absolute path to the folder with image
    '''

    def __init__(self, sender, password, smtp_name, smtp_port, signature_img_name, signature_img_path, attachment_name,
                 attachment_path):
        super().__init__(sender, password, smtp_name, smtp_port)
        self.signature_img_name = signature_img_name
        self.signature_img_path = signature_img_path
        self.attachment_name = attachment_name
        self.attachment_path = attachment_path

    def create_signature_image_object(self):
        img = open(self.signature_img_path + self.signature_img_name, 'rb')
        sgn_image = MIMEImage(img.read())
        sgn_image.add_header('Content-ID', '<signature_image>')
        return sgn_image

    def create_attachment_object(self):
        binary = open(self.attachment_path + self.attachment_name, 'rb')
        payload = MIMEBase('application', 'octate-stream', Name=self.attachment_name)
        payload.set_payload(binary.read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Decomposition', 'attachment', filename=self.attachment_name)
        return payload

    def send_mail_with_attachment(self, receiver, subject, body):
        '''
        In body, please notice that signature img is denoted by a tag:
        <img src="cid:signature_image">
        it has to be at the end of html body of mail.
        Method calls other class methods to create objects as image and payload to use in mail.
        Image is a signature image.
        Payload is any attachment to the mail.
        '''
        attachment_mail = Mail(self, receiver, subject, body)
        image = self.create_signature_image_object()
        payload = self.create_attachment_object()
        attachment_mail.message.attach(image)
        attachment_mail.message.attach(payload)
        attachment_mail.create_session()
        attachment_mail.attach_message()
        attachment_mail.send_mail()
