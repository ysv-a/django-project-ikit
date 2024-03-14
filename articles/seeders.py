from django_seeding import seeders
from django_seeding.seeder_registry import SeederRegistry
from .models import Article
from faker import Faker
import random
fake = Faker()

# from django.utils import timezone
# timezone.now()
# random.choice([LIST])

@SeederRegistry.register
class CustomSeeder(seeders.Seeder):
    id = 'CustomSeeder2'
    priopity = 1

    def seed(self):
        for _ in range(10):
            article = Article()
            article.name = fake.sentence()
            article.description = fake.text()
            article.characters = fake.random_number(10, False)
            article.save()
