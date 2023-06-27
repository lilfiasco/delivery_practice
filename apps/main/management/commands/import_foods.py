import csv
from django.core.files import File
from main.models import Food, Franchise, Category
from django.core.management.base import BaseCommand
from django.utils.text import slugify
import cyrtranslit
from PIL import Image

class Command(BaseCommand):
    help = 'Импортировать данные из CSV файла в модель Food'

    
    def handle(self, *args, **options):
        csv_file_path = r'C:\Users\Admin\OneDrive - НАО Карагандинский Технический Университет\Рабочий стол\мобвеб\parser\franch_cluster.csv'
        default_photo_path = r'C:\\Users\\Admin\\OneDrive - НАО Карагандинский Технический Университет\\Рабочий стол\\мобвеб\\parser\\photo\\4c242f74-b6d4-11eb-946d-ce279a5c61e0_515d5324_7f05_11ea_8ec4_0a5864675a0b__________1010_544__.jpeg'
        
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                franchise_name = row['Franchise']
                # category_name = row['Category']
                category_name = row['Category'].strip()
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
                franchise_title = franchise.title
                category_title = category.title
                title = food.title
                slug = slugify(cyrtranslit.to_latin(f"{franchise_title}_{category_title}_{title}", "ru"), allow_unicode=True)
                food.slug = slug
                # Save the Food instance
                food.save()



# class Command(BaseCommand):
#     help = 'Импортировать данные из CSV файла в модель Food'

#     def handle(self, *args, **options):
#         csv_file_path = r'C:\Users\Admin\OneDrive - НАО Карагандинский Технический Университет\Рабочий стол\мобвеб\parser\franch_cluster.csv'
#         default_photo_path = r'C:\Users\Admin\OneDrive - НАО Карагандинский Технический Университет\Рабочий стол\мобвеб\parser\photo\28046c20-caa2-11ec-aebf-e29c0b7cf74d_542633a8_c29f_11eb_a2b2_3e73cdc9c0a8_1c27fdb8_0951_11eb_aa9d_c6e1b606c4c4_whopper1_1200_800.jpeg'
        
#         with open(csv_file_path, 'r', encoding='utf-8') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 franchise_name = row['Franchise']
#                 category_name = row['Category'].strip()
#                 food_name = row['Food']
#                 price = int(row['Price'].replace('KZT', '').replace('\xa0', ''))
#                 description = row['Description']
#                 cluster = int(row['Cluster'])
                
#                 franchise = Franchise.objects.get(title=franchise_name)
#                 category = Category.objects.get(title=category_name)

#                 # Create the Food instance
#                 food = Food(
#                     franchise=franchise,
#                     title=food_name,
#                     category=category,
#                     description=description,
#                     price=price,
#                     quantity=25,  # default quantity
#                     cluster=cluster,
#                 )

#                 # Set the default photo
#                 with open(default_photo_path, 'rb') as photo_file:
#                     food.image.save('default_photo4.jpg', File(photo_file), save=False)
                
#                 # Generate the slug
#                 franchise_title = franchise.title
#                 category_title = category.title
#                 title = food.title
#                 slug = slugify(cyrtranslit.to_latin(f"{franchise_title}_{category_title}_{title}", "ru"), allow_unicode=True)
#                 food.slug = slug

#                 # Save the Food instance
#                 food.save()
# class Command(BaseCommand):
#     help = 'Импортировать данные из CSV файла в модель Food'

#     def add_arguments(self, parser):
#         parser.add_argument('csv_file_path', type=str, help='Путь к CSV файлу')
#         parser.add_argument('default_photo_path', type=str, help='Путь к фото по умолчанию')

#     def handle(self, *args, **options):
#         csv_file_path = options['csv_file_path']
#         default_photo_path = options['default_photo_path']
        
#         with open(csv_file_path, 'r', encoding='utf-8') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 franchise_name = row['Franchise']
#                 # category_name = row['Category']
#                 category_name = row['Category'].strip()
#                 food_name = row['Food']
#                 price = int(row['Price'].replace('KZT', '').replace('\xa0', ''))
#                 description = row['Description']
#                 cluster = int(row['Cluster'])
                
#                 franchise = Franchise.objects.get(title=franchise_name)
#                 category = Category.objects.get(title=category_name)

#                 # Create the Food instance
#                 food = Food(
#                     franchise=franchise,
#                     title=food_name,
#                     category=category,
#                     description=description,
#                     price=price,
#                     quantity=25,  # default quantity
#                     cluster=cluster,
#                 )

#                 # Set the default photo
#                 with open(default_photo_path, 'rb') as photo_file:
#                     food.image.save('default_photo.jpg', File(photo_file), save=False)
                
#                 # Save the Food instance
#                 food.save()
