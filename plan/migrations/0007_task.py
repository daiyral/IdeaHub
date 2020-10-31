# Generated by Django 3.1.1 on 2020-10-12 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0006_project_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('body', models.CharField(max_length=128)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('assigned', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.project')),
            ],
        ),
    ]
