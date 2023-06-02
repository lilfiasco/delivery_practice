from django.core.management.base import BaseCommand, CommandError

from auths import models
from main import models
class Command(BaseCommand):
    def add_day_of_weeks(self):
        days=['Первое блюдо','Второе блюдо','Напитки','Десерты','Завтраки','Закуски','Салаты','Пицца','Донер','Гамбургеры','Шашлыки','Суши']
        # if DayOfWeek.objects.all() != []:
        #     return
        for day in days:
            day = models.Category(
                title = day
            )
            day.save()
        
    def handle(self, *args, **options):
        print("Fdfsdf")
        self.add_day_of_weeks()
        
    