from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed database with sample listings'

    def handle(self, *args, **kwargs):
        fake = Faker()
        owner, created = User.objects.get_or_create(username='testuser', defaults={'email': 'test@example.com'})
        if created:
            owner.set_password('password123')
            owner.save()

        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=5),
                location=fake.city(),
                price_per_night=round(random.uniform(50, 500), 2),
                owner=owner
            )

        self.stdout.write(self.style.SUCCESS('Database seeded with sample listings'))
