import random
import string


def generateRandomStringId() -> str:
    randomChars = str.join(string.ascii_letters, string.digits)
    result = ""
    for _ in range(10):
        result += random.choice(randomChars)
    return result
