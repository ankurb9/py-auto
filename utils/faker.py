from faker import Faker


def get_faker(seed=None):
    fake: Faker= Faker()
    if seed:
        fake.seed_instance(seed)
    return fake