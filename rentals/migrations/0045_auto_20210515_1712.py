# Generated by Django 3.1.7 on 2021-05-15 17:12

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0044_auto_20210515_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='userv2.png', force_format=None, keep_meta=True, null=True, quality=0, size=[139, 156], upload_to='customerpics'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='picture',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='userv2.png', force_format=None, keep_meta=True, null=True, quality=0, size=[139, 156], upload_to='staffpics'),
        ),
    ]