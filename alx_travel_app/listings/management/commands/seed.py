from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        Listing.objects.all().delete()
        locations = ['Nairobi', 'Mombasa', 'Kisumu', 'Eldoret']
        for i in range(10):
            Listing.objects.create(
                title=f"Listing {i+1}",
                description="A wonderful place to stay.",
                price_per_night=random.randint(2000, 10000),
                location=random.choice(locations),
                available=True
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database.'))
