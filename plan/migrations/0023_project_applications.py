# Generated by Django 3.1.1 on 2020-10-26 13:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0022_auto_20201025_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='applications',
            field=models.ManyToManyField(blank=True, related_name='applications', to=settings.AUTH_USER_MODEL),
        ),
    ]
