# Generated by Django 4.0 on 2022-01-24 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_contactus_subject_contactus_contactnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='contactNumber',
            field=models.IntegerField(null=True),
        ),
    ]