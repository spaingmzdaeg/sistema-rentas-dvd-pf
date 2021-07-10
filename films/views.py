from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Actor,Film,FilmActor,Language,Category,Language,FilmCategory
from .forms import ActorForm,FilmActorForm,FilmForm,CategoryForm,LanguageForm,FilmCategoryForm
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user,allowed_users,admin_only
# Create your views here.

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def actors(request):
    actors = Actor.objects.all()
    return render(request,'films/actors.html',{'actors':actors})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def addNewActor(request):  
    if request.method == "POST":  
        form = ActorForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect("actors")  
            except:  
                pass 
    else:  
        form = ActorForm()  
    return render(request,'films/actors_form.html',{'form':form})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def editActor(request,id):
    actor = Actor.objects.get(actor_id=id)  
    return render(request,'films/actors_form_update.html', {'actor':actor})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def updateActor(request, id):  
    actor = Actor.objects.get(actor_id=id)  
    form = ActorForm(request.POST,request.FILES, instance = actor)  
    if form.is_valid():  
        form.save()  
        return redirect("actors")  
    return render(request, 'films/actors_form_update.html', {'actor': actor})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def deleteActor(request, id):  
    actor = Actor.objects.get(actor_id=id)
    if request.method == "POST":
        actor.delete()  
        return redirect("actors")
    context = {'item':actor}
    return render(request,'films/delete.html',context)

@allowed_users(allowed_roles=['admin','manager','employee','user'])
@login_required(login_url='login')    
def films(request):
    films = Film.objects.all()
    #films_actors = films.values_list('actors',flat=True)
    context = {'films':films}
    return render(request,'films/films.html',context)

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def addNewFilm(request):  
    if request.method == "POST":  
        form = FilmForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect("films")  
            except:  
                pass 
    else:  
        form = FilmForm()  
    return render(request,'films/films_form.html',{'form':form})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def editFilm(request,id):
    languages = Language.objects.all()
    film = Film.objects.get(film_id=id) 
    form = FilmForm(request.POST,request.FILES,instance=film)    
    return render(request,'films/films_form_update.html', {'film':film,'form':form,'languages':languages})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def updateFilm(request, id):
    languages = Language.objects.all()
    film = Film.objects.get(film_id=id)  
    form = FilmForm(request.POST,request.FILES,instance=film)  
    if form.is_valid():  
        form.save()  
        return redirect("films")  
    return render(request, 'films/films_form_update.html', {'film': film,'form':form,'languages':languages})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def deleteFilm(request, id):  
    film = Film.objects.get(film_id=id)
    if request.method == "POST":
        film.delete()  
        return redirect("films")
    context = {'item':film}
    return render(request,'films/delete_film.html',context)

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def film_actors(request):
    filmActors = FilmActor.objects.all()
    context = {'filmActors':filmActors}
    return render(request,'films/filmactors.html',context)

'''def addNewFilmActor(request):
    actors_list = Actor.objects.all()
    films_list = Film.objects.all()
    form = FilmActorForm(data_list=actors_list,data_list2 = films_list)
    context = {'form':form}
    return render(request,'films/film_actors_form_2.html',context)'''

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def addNewFilmActor(request):
    actors = Actor.objects.all()
    films = Film.objects.all()  
    if request.method == "POST":  
        form = FilmActorForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect("filmactors") 
            except:  
                pass 
    else:  
        form = FilmActorForm()  
    return render(request,'films/film_actors_form.html',{'form':form,'actors':actors,'films':films})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def addNewFilmActorFromFilms(request):
    actors = Actor.objects.all()
    films = Film.objects.all()  
    if request.method == "POST":  
        form = FilmActorForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect("films") 
            except:  
                pass 
    else:  
        form = FilmActorForm()  
    return render(request,'films/film_actors_form_films.html',{'form':form,'actors':actors,'films':films})    

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def editFilmActor(request,id):
    actors = Actor.objects.all()
    films = Film.objects.all()  
    filmActor = FilmActor.objects.get(id=id)  
    form = FilmActorForm(request.POST,request.FILES,instance=filmActor)    
    return render(request,'films/film_actors_form_update.html', {'films': films,'form':form,'actors':actors,'filmActor':filmActor})    

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def updateFilmActor(request, id):
    actors = Actor.objects.all()
    films = Film.objects.all()  
    filmActor = FilmActor.objects.get(id=id)  
    form = FilmActorForm(request.POST,request.FILES,instance=filmActor)  
    if form.is_valid():  
        form.save()  
        return redirect("filmactors")  
    return render(request, 'films/film_actors_form_update.html', {'films': films,'form':form,'actors':actors,'filmActor':filmActor})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def deleteFilmActor(request, id):  
    filmActor = FilmActor.objects.get(id=id)
    if request.method == "POST":
        filmActor.delete()  
        return redirect("filmactors")
    context = {'item':filmActor}
    return render(request,'films/delete_film_actor.html',context)

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def categories(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request,'films/categories.html',context)

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def addNewCategory(request):  
    if request.method == "POST":  
        form = CategoryForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect("categories")  
            except:  
                pass 
    else:  
        form = CategoryForm()  
    return render(request,'films/categories_form.html',{'form':form})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def editCategory(request,id):
    category = Category.objects.get(category_id=id)  
    return render(request,'films/categories_form_update.html', {'category':category})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def updateCategory(request, id):  
    category = Category.objects.get(category_id=id)  
    form = CategoryForm(request.POST,request.FILES, instance = category)  
    if form.is_valid():  
        form.save()  
        return redirect("categories")  
    return render(request, 'films/categories_form_update.html', {'category': category})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def deleteCategory(request, id):  
    category = Category.objects.get(category_id=id)
    if request.method == "POST":
        category.delete()  
        return redirect("categories")
    context = {'item':category}
    return render(request,'films/delete_category.html',context)

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def languages(request):
    languages = Language.objects.all()
    context = {'languages':languages}
    return render(request,'films/languages.html',context)

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def addNewLanguage(request):  
    if request.method == "POST":  
        form = LanguageForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect("languages")  
            except:  
                pass 
    else:  
        form = LanguageForm()  
    return render(request,'films/languages_form.html',{'form':form})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def editLanguage(request,id):
    language = Language.objects.get(language_id=id)  
    return render(request,'films/languages_form_update.html', {'language':language})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def updateLanguage(request, id):  
    language = Language.objects.get(language_id=id)  
    form = LanguageForm(request.POST,request.FILES, instance = language)  
    if form.is_valid():  
        form.save()  
        return redirect("languages")  
    return render(request, 'films/languages_form_update.html', {'language': language})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def deleteLanguage(request, id):  
    language = Language.objects.get(language_id=id)
    if request.method == "POST":
        language.delete()  
        return redirect("languages")
    context = {'item':language}
    return render(request,'films/delete_language.html',context)

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def film_categories(request):
    filmCategories = FilmCategory.objects.all()
    context = {'filmCategories':filmCategories}
    return render(request,'films/filmcategories.html',context)            

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def addNewFilmCategory(request):
    categories = Category.objects.all()
    films = Film.objects.all()  
    if request.method == "POST":  
        form = FilmCategoryForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect("filmcategories")  
            except:  
                pass 
    else:  
        form = FilmCategoryForm()  
    return render(request,'films/film_categories_form.html',{'form':form,'categories':categories,'films':films})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def addNewFilmCategoryFromFilms(request):
    categories = Category.objects.all()
    films = Film.objects.all()  
    if request.method == "POST":  
        form = FilmCategoryForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect("films")  
            except:  
                pass 
    else:  
        form = FilmCategoryForm()  
    return render(request,'films/film_categories_form_films.html',{'form':form,'categories':categories,'films':films})    

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def editFilmCategory(request,id):
    categories = Category.objects.all()
    films = Film.objects.all()  
    filmCategory = FilmCategory.objects.get(id=id)  
    form = FilmCategoryForm(request.POST,request.FILES,instance=filmCategory)    
    return render(request,'films/film_categories_form_update.html', {'films': films,'form':form,'categories':categories,'filmCategory':filmCategory})    

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def updateFilmCategory(request, id):
    categories = Category.objects.all()
    films = Film.objects.all()  
    filmCategory = FilmCategory.objects.get(id=id)  
    form = FilmCategoryForm(request.POST,request.FILES,instance=filmCategory)  
    if form.is_valid():  
        form.save()  
        return redirect("filmcategories")  
    return render(request, 'films/film_categories_form_update.html', {'films': films,'form':form,'categories':categories,'filmCategory':FilmCategory})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def deleteFilmCategory(request, id):  
    filmCategory = FilmCategory.objects.get(id=id)
    if request.method == "POST":
        filmCategory.delete()  
        return redirect("filmcategories")
    context = {'item':filmCategory}
    return render(request,'films/delete_film_category.html',context)

    
