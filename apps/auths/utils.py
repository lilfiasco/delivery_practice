import random


def generate_code() -> str:
    simbols: str = (
        '1234567890'
    )
    code: str = ''
    _: int
    for _ in range(6):
        code += random.choice(simbols)

    return code 
