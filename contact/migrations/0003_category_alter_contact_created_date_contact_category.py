# Generated by Django 5.1.2 on 2024-11-25 21:37

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_picture_contact_show_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2024, 11, 25, 21, 37, 40, 754186, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='contact',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contact.category'),
        ),
    ]
