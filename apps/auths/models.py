#Django
from django.db import models
from django.contrib.auth.base_user import (
    AbstractBaseUser,
    BaseUserManager,
)
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import PermissionsMixin

#Local
from auths.utils import generate_code
from main.models import Franchise, Food


class CustomUserManager(BaseUserManager):
    """Custom User Manager."""

    def create_user(self, phone_number, password):
        if not phone_number:
            raise ValidationError('Phone number is required')

        user = self.model(phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(phone_number, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom User model."""
    username = None
    first_name = models.CharField(
        max_length=150,
        verbose_name='First Name',
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Last Name',
        blank=True,
        null=True,
    )
    phone_regex = RegexValidator(
        regex=r'^\+?[0-9]{1,12}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 12 digits are allowed."
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=12,
        verbose_name='Phone Number',
        unique=True,
    )
    birth_date = models.DateField(
        "Date of Birth",
        blank=True,
        null=True,
    )
    is_superuser = models.BooleanField(
        verbose_name='Superuser',
        default=False
    )
    is_active = models.BooleanField(
        verbose_name='Active',
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name='Staff',
        default=False
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        # app_label = 'auths_customuser'

        ordering = ('-id',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    # def save(self, *args, **kwargs):
    #     self.full_clean()
    #     return super().save(*args, **kwargs)
    

class Coworker(CustomUser):
    """
    Coworker class. Has only 2 diffirences from CustomUser
    """

    is_coworker = models.BooleanField(
        default=True,
        verbose_name="сотрудничающий представитель"
    )
    franchise = models.ForeignKey(
        Franchise,
        on_delete=models.CASCADE,
        verbose_name="франшиза"
    ) 


class Cart(models.Model):
    """
    Cart model.
    """

    customer = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="заказчик"
    )
    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        verbose_name="заказанное блюдо"
    )
    price = models.PositiveIntegerField(
        verbose_name="цена"
    )
    quantity = models.PositiveIntegerField(
        verbose_name="количество",
        default=0
    )

    class Meta:
        ordering = [
            '-id'
        ]
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'

    def __str__(self) -> str:
        return self.price


class Order(models.Model):
    """
    Order model.
    """

    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        verbose_name="заказанное блюдо"
    )
    price = models.PositiveIntegerField(
        verbose_name="цена"
    )
    quantity = models.PositiveIntegerField(
        verbose_name="количество",
        default=0
    )
    total_price = models.PositiveIntegerField(
        verbose_name="итоговая цена"
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="заказчик"
    )

    is_done = models.BooleanField(
        default=False,
        verbose_name='оплачено ли'
    )
    datetime_created = models.DateTimeField(
        auto_now=True,
        # default=timezone.now(),
        null=True,
        verbose_name='время заказа'
    )

    class Meta:
        ordering = [
            '-id'
        ]
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self) -> str:
        return self.total_price


class PaymentTypes(models.IntegerChoices):
    """
    Payment types statuses.
    """

    CASH = 1, 'Опата курьеру'
    CARD = 2, 'Оплата картой'


class Purchase(models.Model):
    """
    Purchase model.
    """

    order = models.JSONField()
    payment = models.IntegerField(
        default=PaymentTypes.CASH, choices=PaymentTypes.choices
    )
    # card_number = models.CharField(
    #     max_length=16,
    #     null=True,
    #     verbose_name='номер карты'
    # )
    address = models.CharField(
        max_length=255,
        verbose_name='адрес доставки'
    )


    class Meta:
        ordering = [
            '-id'
        ]
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'
