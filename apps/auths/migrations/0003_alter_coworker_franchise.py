# Generated by Django 4.2.1 on 2023-05-30 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_menufood_foodid_remove_menufood_menuid_and_more'),
        ('auths', '0002_coworker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coworker',
            name='franchise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.franchise', verbose_name='франшиза'),
        ),
    ]
