# Generated by Django 3.1.7 on 2021-03-30 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actor_id', models.AutoField(primary_key=True, serialize=False)),
                ('actor_picture', models.ImageField(upload_to='actorspics')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'actor',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('film_id', models.AutoField(primary_key=True, serialize=False)),
                ('film_cover', models.ImageField(upload_to='filmcovers')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('release_year', models.IntegerField(blank=True, null=True)),
                ('rental_duration', models.SmallIntegerField()),
                ('rental_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('length', models.SmallIntegerField(blank=True, null=True)),
                ('replacement_cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rating', models.TextField(blank=True, choices=[('G', 'G'), ('PG', 'PG'), ('R', 'R'), ('NC-17', 'NC-17')], default='G')),
                ('special_features', models.TextField(blank=True)),
                ('full_text', models.TextField()),
            ],
            options={
                'db_table': 'film',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('language_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('last_update', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'language',
            },
        ),
        migrations.CreateModel(
            name='FilmCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.category')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film')),
            ],
            options={
                'db_table': 'film_category',
            },
        ),
        migrations.CreateModel(
            name='FilmActor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.actor')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film')),
            ],
            options={
                'db_table': 'film_actor',
            },
        ),
        migrations.AddField(
            model_name='film',
            name='actors',
            field=models.ManyToManyField(through='films.FilmActor', to='films.Actor'),
        ),
        migrations.AddField(
            model_name='film',
            name='categories',
            field=models.ManyToManyField(through='films.FilmCategory', to='films.Category'),
        ),
        migrations.AddField(
            model_name='film',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.language'),
        ),
        migrations.AddField(
            model_name='film',
            name='original_language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filmAsOriginalLanguage', to='films.language'),
        ),
        migrations.AddField(
            model_name='category',
            name='films',
            field=models.ManyToManyField(through='films.FilmCategory', to='films.Film'),
        ),
        migrations.AddField(
            model_name='actor',
            name='films',
            field=models.ManyToManyField(through='films.FilmActor', to='films.Film'),
        ),
    ]
