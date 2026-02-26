import random

from faker import Faker

fake = Faker("en_US")


def generate_random_name(min_length=10):
    while True:
        name = fake.name()
        if len(name) >= min_length:
            return name


def generate_random_email(domain="test.com", min_length=6):
    while True:
        first = fake.first_name().lower()
        last = fake.last_name().lower()
        number = random.randint(10, 9999)
        email = f"{first}.{last}{number}@{domain}"

        if len(email) >= min_length:
            return email


def generate_us_phone():
    first_digit = str(random.randint(2, 9))
    remaining_digits = "".join(str(random.randint(0, 9)) for _ in range(9))
    return first_digit + remaining_digits
