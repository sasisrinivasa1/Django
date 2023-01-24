from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six, threading

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self,user, timestamp):
        return six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
generate_token = TokenGenerator()

class EmailThread(threading.Thread):
    def __init__(self,email):
        self.email = email
        threading.Thread.__init__(self)
    def run(self):
        self.email.send()
        print("Sent Email")

