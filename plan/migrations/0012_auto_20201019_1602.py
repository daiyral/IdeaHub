# Generated by Django 3.1.1 on 2020-10-19 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0011_auto_20201015_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='col',
        ),
        migrations.AddField(
            model_name='task',
            name='col',
            field=models.CharField(blank=True, default='backlog', max_length=32),
        ),
        migrations.DeleteModel(
            name='Cols',
        ),
    ]
