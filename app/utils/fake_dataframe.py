import random

import faker
from faker_music import MusicProvider

# create some fake data
fake = faker.Faker()
fake.add_provider(MusicProvider)


def make_music(num):
    """function to create a dataframe with fake values"""
    fake_music = [
        {
            "Song Name": random.choice(["Heavy metal", "Jazz", "Blues", "Rock", "Pop"]),
            "Date": fake.date_between(start_date="-2d", end_date="today"),
            "Number of Plays": random.randint(10, 300),
        }
        for x in range(num)
    ]

    return fake_music
