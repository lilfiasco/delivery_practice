import csv
from django.core.files import File
from main.models import Food, Franchise, Category


def import_foods_from_csv(csv_file_path, default_photo_path):
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            franchise_name = row['Franchise']
            category_name = row['Category']
            food_name = row['Food']
            price = int(row['Price'].replace('KZT', '').replace('\xa0', ''))
            description = row['Description']
            cluster = int(row['Cluster'])
            
            franchise = Franchise.objects.get(title=franchise_name)
            category = Category.objects.get(title=category_name)

            # Create the Food instance
            food = Food(
                franchise=franchise,
                title=food_name,
                category=category,
                description=description,
                price=price,
                quantity=25,  # default quantity
                cluster=cluster,
            )

            # Set the default photo
            with open(default_photo_path, 'rb') as photo_file:
                food.image.save('default_photo.jpg', File(photo_file), save=False)
            
            # Save the Food instance
            food.save()

# Usage
csv_file_path = r'C:\Users\Admin\OneDrive - НАО Карагандинский Технический Университет\Рабочий стол\мобвеб\parser\franch_cluster.csv'
default_photo_path = r'C:\path\to\default_photo.jpg'  # Replace with the actual path to the default photo
import_foods_from_csv(csv_file_path, default_photo_path)