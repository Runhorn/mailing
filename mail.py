import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mail:
    '''
    Mail class has all basic methods which are required to send plain text (html) mail.
    Input:
    user - user object
    receiver - str, email address format
    subject - str
    body - html type
    '''

    def __init__(self, user, receiver, subject, body):
        self.sender = user.sender
        self.password = user.password
        self.smtp_name = user.smtp_name
        self.smtp_port = user.smtp_port
        self.session = None
        self.text = None
        self.receiver = receiver
        self.body = body
        self.message = MIMEMultipart()
        self.message['From'] = self.sender
        self.message['To'] = receiver
        self.message['Subject'] = subject

    def create_session(self):
        self.session = smtplib.SMTP(self.smtp_name, self.smtp_port)
        self.session.starttls()
        self.session.login(self.sender, self.password)

    def attach_message(self):
        self.message.attach(MIMEText(self.body, 'html'))
        self.text = self.message.as_string()

    def send_mail(self):
        self.session.sendmail(self.sender, self.receiver, self.text)
        self.session.quit()
        self.session = None
        self.text = None
