# Generated by Django 3.1.7 on 2021-03-31 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_remove_actor_films'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='films',
            field=models.ManyToManyField(through='films.FilmActor', to='films.Film'),
        ),
    ]
