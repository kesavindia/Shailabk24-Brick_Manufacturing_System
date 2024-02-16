'''Implement a class Email with an instance method send() that
simulates sending an email and prints the sender, receiver, and message content.'''

class Email:
    def __init__(self,sender,receiver,message_content="Hello"):
        self.sender = sender
        self.receiver = receiver
        self.message_content = message_content

    def send(self):
        print(f"Email sent!\nSender:{self.sender}\nReceiver:{self.receiver}\n{self.message_content}")
email = Email("sender@example.com", "receiver@example.com", message_content="Hello, how are you?")
email.send()