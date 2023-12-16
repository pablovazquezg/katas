# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
import string


def rot13(message):
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    rotated = alphabet[13:] + alphabet[:13]
    table = str.maketrans(alphabet, rotated)
    return message.translate(table).lower()


text = "Test"
print(rot13(text))  # Prints grfg
