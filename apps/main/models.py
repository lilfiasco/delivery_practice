from django.db import models
from django.utils.text import slugify
from PIL import Image, UnidentifiedImageError
from django.core.exceptions import ValidationError

class Franchise(models.Model):
    """
    Single franchise info model.
    """

    title = models.CharField(
        max_length=255,
        verbose_name="название"
    )
    image = models.ImageField(
        upload_to="media/",
        verbose_name="изображение",
        null=True
        # validators=[validate_image_size]
    )
    address = models.CharField(
        max_length=255,
        verbose_name="адрес"
    )

    class Meta:
        ordering = [
            '-id'
        ]
        verbose_name = 'франшиза'
        verbose_name_plural = 'франшизы'

    def __str__(self) -> str:
        return self.title
    

class Category(models.Model):
    """
    Class for category info.
    """

    title = models.CharField(
        max_length=255,
        verbose_name="название"
    )

    class Meta:
        ordering = [
            '-id'
        ]
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self) -> str:
        return self.title
    

class Food(models.Model):
    """
    Current dish info.
    """
    franchise = models.ForeignKey(
        to = Franchise,
        blank=True,
        null=True,
        verbose_name='франшиза',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=255,
        verbose_name="название"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True
    )
    description = models.TextField(
        verbose_name="описание"
    )
    price = models.PositiveIntegerField(
        verbose_name="цена"
    )
    image = models.ImageField(
        upload_to="media/",
        verbose_name="изображение",
        # validators=[validate_image_size]
    )
    slug = models.SlugField(
        max_length=255,
        unique=True, 
        blank=True, 
        null=True
    )
    quantity = models.PositiveIntegerField(
        default=25,
        verbose_name="количество еды",
        null=True
    )
    cluster = models.PositiveIntegerField(
        verbose_name="кластер",null= True
    )
    def save(self, *args, **kwargs):
        if self.image:
            try:
                super(Food, self).save(*args, **kwargs)
                img = Image.open(self.image.path)
                if img.height > 150 or img.width > 150:
                    output_size = (150, 150)
                    img.resize(output_size)
                    img.save(self.image.path)
            except (IOError, OSError, ValidationError, UnidentifiedImageError) as e:
                # Handle the exception (e.g., log an error message, set a default image, etc.)
                print(f"Error occurred while processing image: {e}")
        super(Food, self).save(*args, **kwargs)
    class Meta:
        ordering = [
            '-id'
        ]
        verbose_name = 'блюдо'
        verbose_name_plural = 'блюда'

    def __str__(self) -> str:
        return self.title
    




# from main.filters import validate_image_size

# class Restaurant(models.Model):
#     """
#     Current subsidiary info model.
#     """

#     franchise = models.ForeignKey(
#         Franchise,
#         on_delete=models.SET_NULL,
#         null=True
#     )
#     title = models.CharField(
#         max_length=255,
#         verbose_name="название"
#     )
#     address = models.CharField(
#         max_length=255,
#         verbose_name="адрес"
#     )
#     menu = models.ForeignKey(
#         "Menu",
#         on_delete=models.CASCADE
#     )

#     class Meta:
#         ordering = [
#             '-id'
#         ]
#         verbose_name = 'ресторан'
#         verbose_name_plural = 'рестораны'

#     def __str__(self) -> str:
#         return self.title