import base64
import re


def encode_base64(number):
    return base64.b64encode(str(number).encode()).decode()


def decode_base64(encoded_string):
    match = re.search(r'"(.*?)"', encoded_string)
    extracted_string = match.group(1)
    return base64.b64decode(extracted_string).decode()
