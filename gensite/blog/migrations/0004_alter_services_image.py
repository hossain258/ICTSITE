# Generated by Django 4.0 on 2022-02-23 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_services_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(blank=True, upload_to='services_images'),
        ),
    ]
