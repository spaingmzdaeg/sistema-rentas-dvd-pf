from django.urls import path
from .import views

urlpatterns = [
    path('countries',views.countries,name="countries"),
    path('addnewcountry',views.addNewCountry,name='addnewcountry'),
    path('editcountry/<int:id>', views.editCountry,name='editcountry'),
    path('updatecountry/<int:id>', views.updateCountry,name='updatecountry'),
    path('deletecountry/<int:id>', views.deleteCountry,name='deletecountry'),
    path('cities',views.cities,name="cities"),
    path('addnewcity',views.addNewCity,name='addnewcity'),
    path('editcity/<int:id>', views.editCity,name='editcity'),
    path('updatecity/<int:id>', views.updateCity,name='updatecity'),
    path('deletecity/<int:id>', views.deleteCity,name='deletecity'),
    path('addresses',views.addresses,name="addresses"),
    path('addnewaddress',views.addNewAddress,name='addnewaddress'),
    path('editaddress/<int:id>', views.editAddress,name='editaddress'),
    path('updateaddress/<int:id>', views.updateAddress,name='updateaddress'),
    path('deleteaddress/<int:id>', views.deleteAddress,name='deleteaddress'),
    
]
