# Generated by Django 3.1.7 on 2021-05-13 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0038_staff_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
