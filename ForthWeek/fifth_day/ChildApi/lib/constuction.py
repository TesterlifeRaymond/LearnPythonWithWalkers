
""" pass """
import random
import string


class Construction:
    """ pass """
    @classmethod
    def mobile(cls):
        """ pass """
        enum = [130, 131, 132, 133, 135, 137, 139, 140, 155, 170, 188]
        return str(random.choice(enum)) + str(random.randint(10000000, 99999999))

    @classmethod
    def password(cls, num=8):
        """ pass """
        chars = string.ascii_letters + string.digits
        return ''.join(random.sample(list(chars), num))
