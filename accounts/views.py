from addresses.models import Address
from django.shortcuts import render,redirect,get_object_or_404
from rentals.models import Inventory,Customer,Rental,Staff,Customer,Store
from addresses.models import City
from rentals.forms import RentalForm,CustomerForm,StaffForm
from addresses.forms import AddressForm
from django.http import HttpResponse
from django.db.models import Count

from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user,allowed_users,admin_only
from django import template
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages 

# Create your views here.



@unauthenticated_user
def registerPage(request):
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')

                group =  Group.objects.get(name='user')
                user.groups.add(group)
                Customer.objects.create(
                    user=user,
                    email = str(user.email),
                    first_name = str(user.first_name),
                    last_name = str(user.last_name),
                )

                messages.success(request, 'Account was created for ' + username )

                return redirect('login')

        context = {'form':form}
        return render(request,'accounts/register.html',context)

@unauthenticated_user
def loginPage(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Username OR password incorrect')

        context = {}
        return render(request,'accounts/login.html',context)    

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    labels = []
    data = []
    inventories = Inventory.objects.all()
    rentals = Rental.objects.all()
    customers = Customer.objects.all()
    totalFilms = inventories.count()
    rentalFilms = rentals.count()
    activeCustomers = customers.filter(activebool=True).count()
    inactiveCustomers = customers.filter(activebool=False).count()
    return render(request,'accounts/dashboard.html',{'labels':['Active','Inactive'],'data':[activeCustomers,inactiveCustomers],'totalFilms':totalFilms,'rentalFilms':rentalFilms,'activeCustomers':activeCustomers,'customers':customers,'rentals':rentals})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','manager','employee'])
def customer(request,id):
    customer = Customer.objects.get(customer_id=id)
    rentals = customer.rental_set.all()
    rentalsNumber = rentals.count()
    #myFilter = PedidoFilter(request.GET,queryset=pedidos)
    #pedidos = myFilter.qs
    context = {'customer':customer,'rentals':rentals,'rentalsNumber':rentalsNumber}
    return render(request,'accounts/customer.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','manager','employee'])
def createNewRental(request,id):
    inventories = Inventory.objects.all()
    #customers = Customer.objects.all()
    staffList = Staff.objects.all()
    customers = Customer.objects.all()
    customer = Customer.objects.get(customer_id=id)
    if request.method == "POST":  
        form = RentalForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect("rentals")  
            except:  
                pass 
    else:  
        form = RentalForm()  
    return render(request,'accounts/rental_form.html',{'form':form,'customers':customers,'inventories':inventories,'customer':customer,'staffList':staffList})    

#vistas para graficas
@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def pie_chart(request):
    labels = []
    data = []
    customers = Customer.objects.all()
    activeCustomers = customers.filter(activebool=True).count()
    inactiveCustomers = customers.filter(activebool=False).count()
    
    return render(request,'accounts/pie_chart.html', {
        'labels':['Active','Inactive'],
        'data':[activeCustomers,inactiveCustomers],
    })    

@allowed_users(allowed_roles=['admin','manager','employee','user'])
@login_required
def userPage(request):
    rentals = request.user.customer.rental_set.all()
    rentalFilms = rentals.count()
    inventories = Inventory.objects.all()
    totalFilms = inventories.count()
    context = {'rentals':rentals,'rentalFilms':rentalFilms,'totalFilms':totalFilms}
    return render(request, 'accounts/user.html', context)

@allowed_users(allowed_roles=['admin','manager'])
@login_required
def managerPage(request):
    labels = []
    data = []
    storeFromManager = Store.objects.get(manager_staff = request.user.staff.staff_id)
    inventories = Inventory.objects.filter(store = storeFromManager.store_id)
    rentals = Rental.objects.select_related('inventory__store').filter(inventory__store = storeFromManager.store_id)
    customers = Customer.objects.filter(store = storeFromManager.store_id)
    totalFilms = inventories.count()
    rentalFilms = rentals.count()
    activeCustomers = customers.filter(activebool=True).count()
    inactiveCustomers = customers.filter(activebool=False).count()
    context = {'labels':['Active','Inactive'],'data':[activeCustomers,inactiveCustomers],'inventories':inventories,'customers':customers,'rentals':rentals,'totalFilms':totalFilms,'rentalFilms':rentalFilms,'activeCustomers':activeCustomers,'inactiveCustomers':inactiveCustomers}
    return render(request, 'accounts/manager.html', context)

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required
def employeePage(request):
    storeFromStaff = request.user.staff.store.store_id 
    inventories = Inventory.objects.filter(store = storeFromStaff)
    rentals = Rental.objects.select_related('inventory__store').filter(inventory__store = storeFromStaff)
    totalFilms = inventories.count()
    rentalFilms = rentals.count()
    context = {'inventories':inventories,'rentals':rentals,'totalFilms':totalFilms,'rentalFilms':rentalFilms}
    return render(request, 'accounts/employee.html', context)

@login_required
@allowed_users(allowed_roles=['manager','employee','user'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance = customer)
    stores = Store.objects.all()

    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()


    context  = {'form':form,'stores':stores}
    return render(request, 'accounts/account_settings.html', context)

@login_required
@allowed_users(allowed_roles=['manager','employee'])
def accountSettingsEmployees(request):
    staff = request.user.staff
    form = StaffForm(instance = staff)
    addresses = Address.objects.all()
    stores = Store.objects.all()

    if request.method == 'POST':
        form = StaffForm(request.POST,request.FILES,instance=staff)
        if form.is_valid():
            form.save()

    context  = {'form':form,'stores':stores,'addresses':addresses}
    return render(request, 'accounts/account_settings_staff.html', context)
        


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "accounts/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:

						return HttpResponse('Invalid header found.')
						
					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect ("login")
			messages.error(request, 'An invalid email has been entered.')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="accounts/password_reset.html", context={"password_reset_form":password_reset_form})

'''
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "accounts/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'vivalarazad@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="accounts/password_reset.html", context={"password_reset_form":password_reset_form})
'''
