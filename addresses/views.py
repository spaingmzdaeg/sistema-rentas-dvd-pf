from django.shortcuts import render,redirect
from .models import Country,City,Address
from .forms import CountryForm,CityForm,AddressForm
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user,allowed_users,admin_only
# Create your views here.

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def countries(request):
    countries = Country.objects.all()
    return render(request,'addresses/countries.html',{'countries':countries})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def addNewCountry(request):  
    if request.method == "POST":  
        form = CountryForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect("countries")  
            except:  
                pass 
    else:  
        form = CountryForm()  
    return render(request,'addresses/country_form.html',{'form':form})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def editCountry(request,id):
    country = Country.objects.get(country_id=id)  
    return render(request,'addresses/country_form_update.html', {'country':country})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def updateCountry(request, id):  
    country = Country.objects.get(country_id=id)  
    form = CountryForm(request.POST,request.FILES, instance = country)  
    if form.is_valid():  
        form.save()  
        return redirect("countries")  
    return render(request, 'addresses/country_form_update.html', {'country': country})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def deleteCountry(request, id):  
    country = Country.objects.get(country_id=id)
    if request.method == "POST":
        country.delete()  
        return redirect("countries")
    context = {'item':country}
    return render(request,'addresses/delete_country.html',context)

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def cities(request):
    cities = City.objects.all()
    return render(request,'addresses/cities.html',{'cities':cities})
    

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def addNewCity(request):  
    if request.method == "POST":  
        form = CityForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect("cities")  
            except:  
                pass 
    else:  
        form = CityForm()  
    return render(request,'addresses/city_form.html',{'form':form})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def editCity(request,id):
    countries = Country.objects.all()
    city = City.objects.get(city_id=id)  
    return render(request,'addresses/city_form_update.html', {'city':city,'countries':countries})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def updateCity(request, id):
    countries = Country.objects.all()  
    city = City.objects.get(city_id=id)  
    form = CityForm(request.POST,request.FILES, instance = city)  
    if form.is_valid():  
        form.save()  
        return redirect("cities")  
    return render(request, 'addresses/city_form_update.html', {'city': city,'countries':countries})

@allowed_users(allowed_roles=['admin','manager','employee'])    
@login_required(login_url='login')    
def deleteCity(request, id):  
    city = City.objects.get(city_id=id)
    if request.method == "POST":
        city.delete()  
        return redirect("cities")
    context = {'item':city}
    return render(request,'addresses/delete_city.html',context)

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def addresses(request):
    addresses = Address.objects.all()
    return render(request,'addresses/addresses.html',{'addresses':addresses})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def addNewAddress(request):  
    if request.method == "POST":  
        form = AddressForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect("addresses")  
            except:  
                pass 
    else:  
        form = AddressForm()  
    return render(request,'addresses/address_form.html',{'form':form})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def editAddress(request,id):
    cities = City.objects.all()
    address = Address.objects.get(address_id=id)  
    return render(request,'addresses/address_form_update.html', {'address':address,'cities':cities})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def updateAddress(request, id):
    cities = City.objects.all()  
    address = Address.objects.get(address_id=id)  
    form = AddressForm(request.POST,request.FILES, instance = address)  
    if form.is_valid():  
        form.save()  
        return redirect("addresses")  
    return render(request, 'addresses/address_form_update.html', {'address': address,'cities':cities})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def deleteAddress(request, id):  
    address = Address.objects.get(address_id=id)
    if request.method == "POST":
        address.delete()  
        return redirect("addresses")
    context = {'item':address}
    return render(request,'addresses/delete_address.html',context)                    



