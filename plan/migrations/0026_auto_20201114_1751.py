# Generated by Django 3.1.1 on 2020-11-14 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0025_message_recipient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='requesting',
        ),
        migrations.AddField(
            model_name='user',
            name='invites',
            field=models.ManyToManyField(blank=True, to='plan.Project'),
        ),
    ]
