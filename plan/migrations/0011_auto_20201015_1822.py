# Generated by Django 3.1.1 on 2020-10-15 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0010_auto_20201015_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='col',
            field=models.ManyToManyField(blank=True, default='backlog', to='plan.Cols'),
        ),
    ]