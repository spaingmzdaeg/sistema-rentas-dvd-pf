# Generated by Django 3.1.7 on 2021-03-31 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='picture',
            field=models.ImageField(blank=True, height_field=139, null=True, upload_to='', width_field=156),
        ),
    ]
