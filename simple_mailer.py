import os
from dotenv import dotenv_values
from email.message import EmailMessage


class SimpleMailer:

    email_sender = 'stall84@gmail.com'

    def __init__(self) -> None:
        self.config = dotenv_values(".dev.env")
        self._email_password = self.config['GOOGLE_APP_PASSWORD']

    def add_message(self, message, recipient):
        self.current_message = message
        self.recipient = recipient

    def print_message(self):
        if self.current_message:
            print('recipient: ', self.recipient)
            print('current_message: ', self.current_message)


testMailer = SimpleMailer()
testMailer.add_message('sup bitch', 'tonny3')
testMailer.print_message()
