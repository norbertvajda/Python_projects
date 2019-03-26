import random
import string


class PasswordGenerator:

    @staticmethod
    def generate_salt(str_length=64):
        pass_chars = string.ascii_letters + string.digits + "!#$%&()*+,-./:;<=>?@[]^_{|}~"
        return ''.join(random.choice(pass_chars) for i in range(str_length))
