import csv
from django.core.management.base import BaseCommand
from paldex.models import PalModel

class Command(BaseCommand):
    help = 'Import PAL data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file containing PAL data')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        with open(csv_file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                PalModel.objects.create(
                    name=row['Name'],
                    image=row['Image'],
                    type=row['Type'],
                    skill=row['Skill'],
                    work=row['Work'],
                    drops=row['Drops'],
                    price=row['Price'],
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported data'))

