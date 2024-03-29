# Generated by Django 3.1 on 2022-01-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planer', '0013_auto_20220109_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Rental',
        ),
        migrations.RemoveField(
            model_name='area',
            name='address',
        ),
        migrations.RemoveField(
            model_name='area',
            name='geolocation',
        ),
    ]
