from mail import Mail


class User:
    '''
    Base class for creating plain html mails without attachments.
    Input:
    sender - str, email format
    password - str
    smtp_name - str
    smtp_port - int
    '''

    def __init__(self, sender, password, smtp_name, smtp_port):
        self.sender = sender
        self.password = password
        self.smtp_name = smtp_name
        self.smtp_port = smtp_port

    def send_plain_mail(self, receiver, subject, body):
        '''
        User uses Mail class object, receiver and subject strings and body html message
        This method does all the logic script
        create_session method creates SMTP session for the User to login in e-mail acc
        attach_message attaches html body to the message object of mail
        send_mail ends session and sends e-mail to receiver
        '''
        plain_mail = Mail(self, receiver, subject, body)
        plain_mail.create_session()
        plain_mail.attach_message()
        plain_mail.send_mail()
