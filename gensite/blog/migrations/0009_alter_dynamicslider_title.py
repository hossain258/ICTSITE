# Generated by Django 4.0 on 2022-02-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_dynamicslider_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynamicslider',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]