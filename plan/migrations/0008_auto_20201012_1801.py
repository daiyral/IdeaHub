# Generated by Django 3.1.1 on 2020-10-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0007_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cols',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='col',
            field=models.ManyToManyField(to='plan.Cols'),
        ),
    ]
