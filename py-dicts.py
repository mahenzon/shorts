import random
import string

from faker import Faker

fake = Faker()


def random_string(length):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def random_dict(num_inner_dicts=3, max_depth=3):
    """Generate a random dictionary with several inner dictionaries."""
    if max_depth <= 0:
        return random_string(10)
    else:
        result = {}
        for i in range(num_inner_dicts):
            key = random_string(10)
            value = random_dict(num_inner_dicts, max_depth-1)
            result[key] = value
        return result

# Example usage
my_dict = random_dict(num_inner_dicts=3, max_depth=3)
# print(my_dict)

print(fake.pydict())

print({'gun': 1197, 'bit': 'bob97@example.org', 'nice': 'https://warner-ferguson.net/privacy.htm', 'foot': 'GBRSvRPiAMwWfpEVWYOq', 'police': 'james74@example.com', 'ability': {'indeed': 'aaronlarson@example.org', 'hope': 'AebIPyAATmycHEdGtuJW', 'before': 291,}, 'together': 'VwtvNSBfNHHKFTsFNlDb'})