# Generated by Django 4.0 on 2022-03-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_services_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]