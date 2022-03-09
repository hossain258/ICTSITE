# Generated by Django 4.0 on 2022-02-02 15:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1200)),
            ],
        ),
        migrations.AddField(
            model_name='contactus',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='description',
            field=models.TextField(max_length=1200),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(max_length=1200),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='phone_Number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
