from string import ascii_letters, digits
from random import choices


def get_random_password(n=8) -> str:
    symbols_ = ascii_letters + digits
    list_numbers = choices(symbols_, k=n)
    return ''.join(list_numbers)


print(get_random_password())
# task5
