# Generated by Django 5.1.2 on 2024-10-26 23:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('created_date', models.DateField(default=datetime.datetime(2024, 10, 26, 23, 54, 14, 19429, tzinfo=datetime.timezone.utc))),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
