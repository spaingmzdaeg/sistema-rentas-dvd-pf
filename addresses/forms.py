
from django import forms
from .models import Country,City,Address

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['country']
    def __init__(self, *args, **kwargs):
        super(CountryForm, self).__init__(*args, **kwargs)
        self.fields['country'].widget.attrs['placeholder'] = 'ingrese pais'

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['city','country']
    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        self.fields['city'].widget.attrs['placeholder'] = 'ingrese ciudad'

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address','address2','district','city','postal_code','phone']
    def __init__(self,*args, **kwargs):
        super(AddressForm,self).__init__(*args, **kwargs)
        self.fields['address'].widget.attrs['placeholder'] = 'ingrese direccion'
        self.fields['address2'].widget.attrs['placeholder'] = 'insert direccion opcional'
        self.fields['district'].widget.attrs['placeholder'] = 'ingrese distrito'
        self.fields['city'].widget.attrs['placeholder'] = 'ingrese ciudad'
        self.fields['postal_code'].widget.attrs['placeholder'] = 'ingrese codigo postal'
        self.fields['phone'].widget.attrs['placeholder'] = 'ingrese telefono'



    