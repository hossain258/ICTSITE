# Generated by Django 4.0 on 2021-12-19 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aboutus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('heading', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=700)),
            ],
        ),
    ]
