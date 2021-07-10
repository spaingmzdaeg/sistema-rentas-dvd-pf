from django.urls import path
from . import views

urlpatterns = [
    path('actors', views.actors,name="actors"),
    path('addnewactor',views.addNewActor,name='addnewactor'),
    path('editactor/<int:id>', views.editActor,name='editactor'),
    path('updateactor/<int:id>', views.updateActor,name='updateactor'),
    path('deleteactor/<int:id>', views.deleteActor,name='deleteactor'),
    path('films', views.films,name="films"),
    path('addnewfilm',views.addNewFilm,name='addnewfilm'),
    path('editfilm/<int:id>', views.editFilm,name='editfilm'),
    path('updatefilm/<int:id>', views.updateFilm,name='updatefilm'),
    path('deletefilm/<int:id>', views.deleteFilm,name='deletefilm'),
    path('filmactors', views.film_actors,name="filmactors"),
    path('addnewfilmactor',views.addNewFilmActor,name='addnewfilmactor'),
    path('editfilmactor/<int:id>', views.editFilmActor,name='editfilmactor'),
    path('updatefilmactor/<int:id>', views.updateFilmActor,name='updatefilmactor'),
    path('deletefilmactor/<int:id>', views.deleteFilmActor,name='deletefilmactor'),
    path('categories', views.categories,name="categories"),
    path('addnewcategory',views.addNewCategory,name='addnewcategory'),
    path('editcategory/<int:id>', views.editCategory,name='editcategory'),
    path('updatecategory/<int:id>', views.updateCategory,name='updatecategory'),
    path('deletecategory/<int:id>', views.deleteCategory,name='deletecategory'),
    path('languages', views.languages,name="languages"),
    path('addnewlanguage',views.addNewLanguage,name='addnewlanguage'),
    path('editlanguage/<int:id>', views.editLanguage,name='editlanguage'),
    path('updatelanguage/<int:id>', views.updateLanguage,name='updatelanguage'),
    path('deletelanguage/<int:id>', views.deleteLanguage,name='deletelanguage'),
    path('filmcategories', views.film_categories,name="filmcategories"),
    path('addnewfilmcategory',views.addNewFilmCategory,name='addnewfilmcategory'),
    path('editfilmcategory/<int:id>', views.editFilmCategory,name='editfilmcategory'),
    path('updatefilmcategory/<int:id>', views.updateFilmCategory,name='updatefilmcategory'),
    path('deletefilmcategory/<int:id>', views.deleteFilmCategory,name='deletefilmcategory'),
    path('addnewfilmactorfromfilms',views.addNewFilmActorFromFilms,name='addnewfilmactorfromfilms'),
    path('addnewfilmcategoryfromfilms',views.addNewFilmCategoryFromFilms,name='addnewfilmcategoryfromfilms'),
    

    
   
    
]
