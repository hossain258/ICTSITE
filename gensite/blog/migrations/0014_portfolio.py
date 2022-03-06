# Generated by Django 4.0 on 2022-03-06 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_services_thumbnail_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='portfolio')),
            ],
        ),
    ]