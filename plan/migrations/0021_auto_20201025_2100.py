# Generated by Django 3.1.1 on 2020-10-25 19:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0020_auto_20201025_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='budget',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=64, validators=[django.core.validators.MaxLengthValidator(64)]),
        ),
    ]