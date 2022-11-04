import os
from dotenv import dotenv_values
import ssl
import smtplib
from email.message import EmailMessage


class SimpleMailer:

    email_sender = 'stall84@gmail.com'

    def __init__(self) -> None:
        self.config = dotenv_values(".dev.env")
        self._email_password = self.config['GOOGLE_APP_PASSWORD']
        self.message_queue = []

    def add_message(self, subject, body, recipient):
        self.current_subject = subject
        self.current_body = body
        self.current_recipient = recipient

    def print_message(self):
        if self.current_body:
            print('recipient: ', self.current_recipient)
            print('current_body: ', self.current_body)

    def _compose_message(self):
        email = EmailMessage()
        email['From'] = self.email_sender
        email['To'] = self.current_recipient
        email['Subject'] = self.current_subject
        email.set_content(self.current_body)
        print('composed message: ', email)
        return email

    def send_message(self):
        msg = self._compose_message()
        print('message: ', msg)
        if msg is not None:
            print('committing to send...')
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.set_debuglevel(1)
                smtp.login(self.email_sender, self._email_password)
                smtp.sendmail(self.email_sender,
                              self.current_recipient, msg.as_string())
                return True


testMailer = SimpleMailer()

testMailer.add_message(
    'Sup Turd?', 'Hey turdman! How have you and the wife been lately?', 'wisih37366@fgvod.com')
testMailer.send_message()
