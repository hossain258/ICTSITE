# Generated by Django 4.0 on 2022-03-02 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_aboutus_heading_alter_aboutus_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='aboutus'),
        ),
    ]
