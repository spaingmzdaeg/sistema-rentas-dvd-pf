from django.db import models
from django_resized import ResizedImageField
# Create your models here.
class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    actor_picture = ResizedImageField(size=[139, 156], default="cover_default.svg",upload_to='actorpics', blank=True, null=True)
    first_name =  models.CharField(max_length=45)
    last_name =  models.CharField(max_length=45)
    last_update = models.DateTimeField(auto_now=True)
    films = models.ManyToManyField('Film',through='FilmActor')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = 'actor'

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField(auto_now=True)
    films = models.ManyToManyField('Film',through='FilmCategory')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
    
class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    film_cover = ResizedImageField(size=[139, 156], default="cover_default.svg",upload_to='moviescovers', blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_year = models.IntegerField(blank=True,null=True)
    language = models.ForeignKey('Language',on_delete=models.CASCADE)
    original_language = models.ForeignKey('Language',blank=True,null=True,related_name='filmAsOriginalLanguage',
    on_delete=models.CASCADE)
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=4,decimal_places=2)
    length = models.SmallIntegerField(blank=True,null=True)
    replacement_cost = models.DecimalField(max_digits=5,decimal_places=2)
    #choices for rating
    G = 'G'
    PG = 'PG'
    PG13 = 'PG-13'
    R='R'
    NC17 = 'NC-17'
    CHOICE_RATING = [
        (G,'G'),
        (PG,'PG'),
        (R,'R'),
        (NC17,'NC-17'),
    ]
    rating = models.TextField(blank=True,choices=CHOICE_RATING,default=G)
    special_features = models.TextField(blank=True)
    #pending
    full_text = models.TextField()
    #pending
    categories = models.ManyToManyField(Category,through='FilmCategory')
    actors = models.ManyToManyField(Actor,through='FilmActor')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'film'

class FilmActor(models.Model):
    actor = models.ForeignKey(Actor,on_delete=models.CASCADE)
    film = models.ForeignKey(Film,on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.actor)+'-'+str(self.film)

    class Meta:
        db_table = 'film_actor'

class FilmCategory(models.Model):
    film = models.ForeignKey(Film,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.category)+'-'+str(self.film)

    class Meta:
        db_table = 'film_category'

class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateField(auto_now=True)

    class Meta:
        db_table = 'language'

    def __str__(self):
        return self.name
                        


    



    

    
