# Generated by Django 3.1.7 on 2021-05-15 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0045_auto_20210515_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='activebool',
            field=models.BooleanField(default=True),
        ),
    ]
