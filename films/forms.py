from django import forms
from .views import Actor
from.models import Actor,Film,FilmActor,Category,Language,FilmCategory
from .fields import ListTextWidget
from django_resized import ResizedImageField

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['actor_picture','first_name','last_name']
        widgets = { 
            'first_name': forms.TextInput(attrs={ 'class': 'form-control','placeholder': 'First Name' }),
            'last_name': forms.TextInput(attrs={ 'class': 'form-control','placeholder': 'Last Name' }),
      }


class FilmForm(forms.ModelForm):
    
    class Meta:
        model = Film
        fields = ['film_cover','title','description','release_year','language','original_language','rental_duration','rental_rate','length','replacement_cost','rating','special_features','full_text']

    def __init__(self, *args, **kwargs):
        super(FilmForm, self).__init__(*args, **kwargs)

        # sets the placeholder key/value in the attrs for a widget
        # when the form is instantiated (so the widget already exists)
        self.fields['title'].widget.attrs['placeholder'] = 'ingrese titulo'
        self.fields['description'].widget.attrs['placeholder'] = 'ingrese descripcion'
        self.fields['release_year'].widget.attrs['placeholder'] = 'ingrese año de lanzamiento'
        self.fields['rental_rate'].widget.attrs['placeholder'] = 'ingrese precio de renta'
        self.fields['length'].widget.attrs['placeholder'] = 'ingrese longitud de renta'
        self.fields['replacement_cost'].widget.attrs['placeholder'] = 'ingrese coste de remplazo'
        self.fields['special_features'].widget.attrs['placeholder'] = 'ingrese caracteristicas especiales'
        self.fields['full_text'].widget.attrs['placeholder'] = 'insert full text'
        self.fields['rental_duration'].widget.attrs['placeholder'] = 'ingrese duracion de renta'
        


class FilmActorForm(forms.ModelForm):
    class Meta:
        model = FilmActor
        fields = ['actor','film']
        #actors = forms.CharField(required=True)
        #films = forms.CharField(required=True)
       
    '''def __init__(self, *args, **kwargs):
        _actor_list = kwargs.pop('data_list',None)
        _film_list = kwargs.pop('data_list2',None)
        super(FilmActorForm,self).__init__(*args, **kwargs)
        self.fields['actors'].widget = ListTextWidget(data_list=_actor_list, name='actor-list')
        self.fields['films'].widget = ListTextWidget(data_list=_film_list, name='film-list')'''

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_id','name']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        # sets the placeholder key/value in the attrs for a widget
        # when the form is instantiated (so the widget already exists)
        self.fields['name'].widget.attrs['placeholder'] = 'insert name'

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['language_id','name']

    def __init__(self, *args, **kwargs):
        super(LanguageForm, self).__init__(*args, **kwargs)

        # sets the placeholder key/value in the attrs for a widget
        # when the form is instantiated (so the widget already exists)
        self.fields['name'].widget.attrs['placeholder'] = 'insert name'

class FilmCategoryForm(forms.ModelForm):
    class Meta:
        model = FilmCategory
        fields = ['category','film']                             
