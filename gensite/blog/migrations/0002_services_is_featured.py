# Generated by Django 4.0 on 2022-03-20 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='is_featured',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
