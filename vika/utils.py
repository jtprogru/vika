
import secrets
import string


def gen(lenght):

    alphabet = string.ascii_uppercase + string.digits
    promo = ''

    for _ in range(lenght):
        promo += ''.join(secrets.choice(alphabet))
    print(promo)


def getpwd(length):
    alphabet = string.ascii_letters + string.digits

    password = ''.join(secrets.choice(alphabet) for _ in range(length))

    print(password)
