# Generated by Django 4.2.2 on 2023-11-29 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_remove_offers_time_offers_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='image',
            field=models.ImageField(upload_to='uploads'),
        ),
    ]
