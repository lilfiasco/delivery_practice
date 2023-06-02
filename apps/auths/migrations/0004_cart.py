# Generated by Django 4.2.1 on 2023-06-01 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_food_options'),
        ('auths', '0003_alter_coworker_franchise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(verbose_name='цена')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='количество')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='заказчик')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.food', verbose_name='заказанное блюдо')),
            ],
            options={
                'verbose_name': 'корзина',
                'verbose_name_plural': 'корзины',
                'ordering': ['-id'],
            },
        ),
    ]
