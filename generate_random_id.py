import random


def generate_id(length):
    return "".join([random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']) for _ in range(length)])
