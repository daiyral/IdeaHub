# Generated by Django 3.1.1 on 2020-10-21 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0016_auto_20201019_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='est_length',
            field=models.TimeField(null=True),
        ),
    ]
