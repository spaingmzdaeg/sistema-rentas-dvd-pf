from django.contrib import admin
from films.models import *
from addresses.models import *
from rentals.models import *

# Register your models here.

admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Film)
admin.site.register(FilmActor)
admin.site.register(FilmCategory)
admin.site.register(Language)
admin.site.register(Address)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Customer)
admin.site.register(Inventory)
admin.site.register(Rental)
admin.site.register(Payment)
admin.site.register(Staff)
admin.site.register(Store)