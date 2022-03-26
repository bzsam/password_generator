import random
import string


# Character types
LOWERCASE = list(string.ascii_lowercase)
UPPERCASE = list(string.ascii_uppercase)
DIGITS = list(string.digits)
PUNCTUATION = list(string.punctuation)
CHAR_LIST = [LOWERCASE, UPPERCASE, DIGITS, PUNCTUATION]


class Password:
    def __init__(self):
        """Password generator module"""
        self.pw = []
        self.num_list = []

    def password(self, pw_min, pw_max):
        """Function to create the password, needs a min and max length value"""
        self.pw = []

        # Generate a number for each character type
        self.num_list = [random.randint(1, 5) for i in range(4)]
        while sum(self.num_list) > pw_max or sum(self.num_list) < pw_min:
            self.num_list = [random.randint(1, 5) for i in range(4)]

        # Takes j number of character from each character type, j is from the generated numbers
        for i in range(4):
            for j in range(self.num_list[i]):
                self.pw.append(random.choice(CHAR_LIST[i]))

        random.shuffle(self.pw)  # Shuffles the created list
        return ''.join(self.pw)
