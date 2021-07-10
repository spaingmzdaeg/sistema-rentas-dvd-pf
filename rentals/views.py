from django.db.models.query import RawQuerySet
from django.shortcuts import render,redirect,get_object_or_404
from .models import Staff,Address,Store,Customer,Inventory,Film,Rental,Payment
from .forms import StaffForm,StoreForm,CustomerForm,InventoryForm,RentalForm,PaymentForm
from django.views.generic import ListView
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import datetime
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user,allowed_users,admin_only
from accounts.forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
# Create your views here.

@allowed_users(allowed_roles=['admin','manager'])
@login_required(login_url='login')
def staff(request):
    if request.user.groups.filter(name = 'manager').exists() or request.user.groups.filter(name='employee'):
        storeFromStaff = request.user.staff.store.store_id
        staffList = Staff.objects.filter(store = storeFromStaff)
    else:
        staffList = Staff.objects.all()    
    return render(request,'rentals/staff_list.html',{'staffList':staffList})


@allowed_users(allowed_roles=['admin','manager'])
@login_required(login_url='login')
def addNewEmployee(request):
    if request.user.groups.filter(name = 'admin').exists():
        stores = Store.objects.all()
    elif request.user.groups.filter(name = 'manager').exists():
        storeFromStaff = request.user.staff.store.store_id
        stores = Store.objects.filter(store_id = storeFromStaff)   
    
    addresses = Address.objects.all()
    form = CreateUserForm()
    form2 = StaffForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        form2 = StaffForm(request.POST,request.FILES)
        if form.is_valid() and form2.is_valid():
            user = form.save()
            #staff = form2.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form2.cleaned_data.get('address')
            store = form2.cleaned_data.get('store')
            active = form2.cleaned_data.get('active')
            picture = form2.cleaned_data.get('picture')

            group = Group.objects.get(name='employee')
            user.groups.add(group)
            Staff.objects.create(
                user=user,
                email = str(user.email),
                first_name = str(user.first_name),
                last_name = str(user.last_name),
                address = address,
                store = store,
                active = active,
                picture = picture
            )

            return redirect('stafflist')

      
    return render(request,'rentals/staff_form.html',{'form':form,'form2':form2,'addresses':addresses,'stores':stores})


'''@allowed_users(allowed_roles=['admin','manager'])
@login_required(login_url='login')
def addNewEmployee(request):
    addresses = Address.objects.all()
    stores = Store.objects.all();  
    if request.method == "POST":  
        form = StaffForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect("stafflist")  
            except:  
                pass 
    else:  
        form = StaffForm()  
    return render(request,'rentals/staff_form.html',{'form':form,'addresses':addresses,'stores':stores})'''


@allowed_users(allowed_roles=['admin','manager'])
@login_required(login_url='login')
def editEmployee(request,id):

    if request.user.groups.filter(name = 'admin').exists():
        stores = Store.objects.all()
    elif request.user.groups.filter(name = 'manager').exists():
        storeFromStaff = request.user.staff.store.store_id
        stores = Store.objects.filter(store_id = storeFromStaff)   

    addresses = Address.objects.all()
    
    employee = Staff.objects.get(staff_id=id)  
    return render(request,'rentals/staff_form_update.html', {'employee':employee,'addresses':addresses,'stores':stores})

@allowed_users(allowed_roles=['admin','manager'])
@login_required(login_url='login')
def updateEmployee(request, id):
    if request.user.groups.filter(name = 'admin').exists():
        stores = Store.objects.all()
    elif request.user.groups.filter(name = 'manager').exists():
        storeFromStaff = request.user.staff.store.store_id
        stores = Store.objects.filter(store_id = storeFromStaff)   
    
    addresses = Address.objects.all()
       
    employee = Staff.objects.get(staff_id=id)  
    form = StaffForm(request.POST,request.FILES, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("stafflist")  
    return render(request, 'rentals/staff_form_update.html', {'employee': employee,'addresses':addresses,'stores':stores})

@allowed_users(allowed_roles=['admin','manager'])
@login_required(login_url='login')
def deleteEmployee(request, id):  
    employee = Staff.objects.get(staff_id=id)
    if request.method == "POST":
        employee.user.delete()  
        return redirect("stafflist")
    context = {'item':employee}
    return render(request,'rentals/delete_staff.html',context)

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def stores(request):
    stores = Store.objects.all()
    return render(request,'rentals/stores.html',{'stores':stores})    

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def addNewStore(request):
    addresses = Address.objects.all()
    employees = Staff.objects.all()
    stores = Store.objects.all();  
    if request.method == "POST":  
        form = StoreForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect("stores")  
            except:  
                pass 
    else:  
        form = StoreForm()  
    return render(request,'rentals/store_form.html',{'form':form,'employees':employees,'addresses':addresses})

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def editStore(request,id):
    addresses = Address.objects.all()
    employees = Staff.objects.all(); 
    store = Store.objects.get(store_id=id)  
    return render(request,'rentals/store_form_update.html', {'employees':employees,'addresses':addresses,'store':store})

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def updateStore(request, id):
    addresses = Address.objects.all()
    employees = Staff.objects.all(); 
    store = Store.objects.get(store_id=id) 
    form = StoreForm(request.POST,request.FILES, instance = store)  
    if form.is_valid():  
        form.save()  
        return redirect("stores")  
    return render(request, 'rentals/store_form_update.html', {'employees': employees,'addresses':addresses,'store':store})

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def deleteStore(request, id):  
    store = Store.objects.get(store_id=id)
    if request.method == "POST":
        store.delete()  
        return redirect("stores")
    context = {'item':store}
    return render(request,'rentals/delete_store.html',context)

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def customers(request):
    if request.user.groups.filter(name = 'manager').exists() or request.user.groups.filter(name='employee').exists():
        storeFromStaff = request.user.staff.store.store_id
        customers = Customer.objects.filter(store = storeFromStaff)
    else:
        customers = Customer.objects.all()    
    return render(request,'rentals/customers.html',{'customers':customers})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def addNewCustomer(request):
    if request.user.groups.filter(name = 'admin').exists():
        stores = Store.objects.all()
    elif request.user.groups.filter(name = 'manager').exists() or request.user.groups.filter(name='employee').exists():
        storeFromStaff = request.user.staff.store.store_id
        stores = Store.objects.filter(store_id = storeFromStaff)   
    
    addresses = Address.objects.all()
    
    form = CreateUserForm()
    form2 = CustomerForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        form2 = CustomerForm(request.POST,request.FILES)
        if form.is_valid() and form2.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form2.cleaned_data.get('address')
            store = form2.cleaned_data.get('store')
            activebool =  form2.cleaned_data.get('activebool')
            active = form2.cleaned_data.get('active')
            profile_pic = form2.cleaned_data.get('profile_pic')

            group = Group.objects.get(name='user')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
                email = str(user.email),
                first_name = str(user.first_name),
                last_name = str(user.last_name),
                address = address,
                store = store,
                active = active,
                activebool = activebool,
                profile_pic = profile_pic
            )

            return redirect('customers')

    return render(request,'rentals/customer_form.html',{'form':form,'form2':form2,'stores':stores,'addresses':addresses})

'''@allowed_users(allowed_roles=['admin','manager'])
@login_required(login_url='login')
def addNewCustomer(request):
    addresses = Address.objects.all()
    stores = Store.objects.all()
    if request.method == "POST":  
        form = CustomerForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect("customers")  
            except:  
                pass 
    else:  
        form = CustomerForm()  
    return render(request,'rentals/customer_form.html',{'form':form,'stores':stores,'addresses':addresses})'''

@allowed_users(allowed_roles=['admin','manager'])
@login_required(login_url='login')
def editCustomer(request,id):
    if request.user.groups.filter(name = 'admin').exists():
        stores = Store.objects.all()
    elif request.user.groups.filter(name = 'manager').exists() or request.user.groups.filter(name='employee').exists():
        storeFromStaff = request.user.staff.store.store_id
        stores = Store.objects.filter(store_id = storeFromStaff)   

    
    addresses = Address.objects.all()
    
    customer = Customer.objects.get(customer_id=id)  
    return render(request,'rentals/customer_form_update.html', {'customer':customer,'addresses':addresses,'stores':stores})

@allowed_users(allowed_roles=['admin','manager'])
@login_required(login_url='login')
def updateCustomer(request, id):
    if request.user.groups.filter(name = 'admin').exists():
        stores = Store.objects.all()
    elif request.user.groups.filter(name = 'manager').exists() or request.user.groups.filter(name='employee').exists():
        storeFromStaff = request.user.staff.store.store_id
        stores = Store.objects.filter(store_id = storeFromStaff)

    
    addresses = Address.objects.all()
    
    customer = Customer.objects.get(customer_id=id) 
    form = CustomerForm(request.POST,request.FILES, instance = customer)  
    if form.is_valid():  
        form.save()  
        return redirect("customers")  
    return render(request, 'rentals/customer_form_update.html', {'customer': customer,'addresses':addresses,'stores':stores})  

@allowed_users(allowed_roles=['admin','manager'])
@login_required(login_url='login')
def deleteCustomer(request, id):  
    customer = Customer.objects.get(customer_id=id)
    if request.method == "POST":
        customer.user.delete()  
        return redirect("customers")
    context = {'item':customer}
    return render(request,'rentals/delete_customer.html',context)

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def inventories(request):
    if request.user.groups.filter(name = 'manager').exists() or request.user.groups.filter(name = 'employee'):
        storeFromStaff = request.user.staff.store.store_id
        inventories = Inventory.objects.filter(store = storeFromStaff)
    else:
        inventories = Inventory.objects.all()    
    
    return render(request,'rentals/inventories.html',{'inventories':inventories})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def addNewInventory(request):
    if request.user.groups.filter(name = 'admin').exists():
        stores = Store.objects.all()
    elif request.user.groups.filter(name = 'manager').exists() or request.user.groups.filter(name = 'employee'):
        storeFromStaff = request.user.staff.store.store_id
        stores = Store.objects.filter(store_id = storeFromStaff)

    
    films = Film.objects.all()
    
    if request.method == "POST":  
        form = InventoryForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect("inventories")  
            except:  
                pass 
    else:  
        form = InventoryForm()  
    return render(request,'rentals/inventory_form.html',{'form':form,'films':films,'stores':stores})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def editInventory(request,id):
    if request.user.groups.filter(name = 'admin').exists():
        stores = Store.objects.all()
    elif request.user.groups.filter(name = 'manager').exists() or request.user.groups.filter(name='employee').exists():
        storeFromStaff = request.user.staff.store.store_id
        stores = Store.objects.filter(store_id = storeFromStaff)   

    films = Film.objects.all()
    
    inventory = Inventory.objects.get(inventory_id=id)  
    return render(request,'rentals/inventory_form_update.html', {'inventory':inventory,'films':films,'stores':stores})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def updateInventory(request, id):
    if request.user.groups.filter(name = 'admin').exists():
        stores = Store.objects.all()
    elif request.user.groups.filter(name = 'manager').exists() or request.user.groups.filter(name='employee').exists():
        storeFromStaff = request.user.staff.store.store_id
        stores = Store.objects.filter(store_id = storeFromStaff)

    
    films = Film.objects.all()
    
    inventory = Inventory.objects.get(inventory_id=id) 
    form = InventoryForm(request.POST,request.FILES, instance = inventory)  
    if form.is_valid():  
        form.save()  
        return redirect("inventories")  
    return render(request, 'rentals/inventory_form_update.html', {'inventory': inventory,'films':films,'stores':stores})          

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def deleteInventory(request, id):  
    inventory = Inventory.objects.get(inventory_id=id)
    if request.method == "POST":
        inventory.delete()  
        return redirect("inventories")
    context = {'item':inventory}
    return render(request,'rentals/delete_inventory.html',context)

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def rentals(request):
    if request.user.groups.filter(name = 'manager').exists() or request.user.groups.filter(name = 'employee').exists():
        storeFromStaff = request.user.staff.store.store_id
        rentals = Rental.objects.select_related('inventory__store').filter(inventory__store = storeFromStaff)
    else:
        rentals = Rental.objects.all()    
    return render(request,'rentals/rentals.html',{'rentals':rentals})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def payments(request):
    if request.user.groups.filter(name = 'manager').exists() or request.user.groups.filter(name = 'employee').exists():
        storeFromStaff = request.user.staff.store.store_id
        payments = Payment.objects.select_related('staff__store').filter(staff__store = storeFromStaff)
    else:
        payments = Payment.objects.all()    

    return render(request,'rentals/payments.html',{'payments':payments})    

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def addNewRental(request):
    if request.user.groups.filter(name = 'manager').exists() or request.user.groups.filter(name = 'employee').exists():
        storeFromStaff = request.user.staff.store.store_id
        inventories = Inventory.objects.filter(store = storeFromStaff)
        customers = Customer.objects.filter(store = storeFromStaff)
        staffList = Staff.objects.filter(store = storeFromStaff)
    else:
        inventories = Inventory.objects.all()
        customers = Customer.objects.all()
        staffList = Staff.objects.all()      

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
    return render(request,'rentals/rental_form.html',{'form':form,'inventories':inventories,'customers':customers,'staffList':staffList})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def editRental(request,id):
    if request.user.groups.filter(name = 'manager').exists() or request.user.groups.filter(name = 'employee').exists():
        storeFromStaff = request.user.staff.store.store_id
        inventories = Inventory.objects.filter(store = storeFromStaff)
        customers = Customer.objects.filter(store = storeFromStaff)
        staffList = Staff.objects.filter(store = storeFromStaff)
    else:
        inventories = Inventory.objects.all()
        customers = Customer.objects.all()
        staffList = Staff.objects.all()
    
    rental = Rental.objects.get(rental_id=id)
    yearRental = rental.get_year_rental()
    monthRental = rental.get_month_rental()
    dayRental = rental.get_day_rental()
    yearReturn = rental.get_year_return()
    monthReturn = rental.get_month_return()
    dayReturn = rental.get_day_return()  
    return render(request,'rentals/rental_form_update.html', {'rental':rental,'customers':customers,'inventories':inventories,'staffList':staffList,'dayRental':dayRental,'monthRental':monthRental,'yearRental':yearRental,'dayReturn':dayReturn,'monthReturn':monthReturn,'yearReturn':yearReturn})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def updateRental(request, id):
    if request.user.groups.filter(name = 'manager').exists() or request.user.groups.filter(name = 'employee').exists():
        storeFromStaff = request.user.staff.store.store_id
        inventories = Inventory.objects.filter(store = storeFromStaff)
        customers = Customer.objects.filter(store = storeFromStaff)
        staffList = Staff.objects.filter(store = storeFromStaff)
    else:
        inventories = Inventory.objects.all()
        customers = Customer.objects.all()
        staffList = Staff.objects.all()

    rental = Rental.objects.get(rental_id=id)
    yearRental = rental.get_year_rental()
    monthRental = rental.get_month_rental()
    dayRental = rental.get_day_rental()
    yearReturn = rental.get_year_return()
    monthReturn = rental.get_month_return()
    dayReturn = rental.get_day_return()
    form = RentalForm(request.POST,request.FILES, instance = rental)  
    if form.is_valid():  
        form.save()  
        return redirect("rentals")  
    return render(request, 'rentals/rental_form_update.html', {'rental': rental,'customers':customers,'inventories':inventories,'staffList':staffList,'dayRental':dayRental,'monthRental':monthRental,'yearRental':yearRental,'dayreturn':dayReturn,'monthReturn':monthReturn,'yearReturn':yearReturn})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def deleteRental(request, id):  
    rental = Rental.objects.get(rental_id=id)
    if request.method == "POST":
        rental.delete()  
        return redirect("rentals")
    context = {'item':rental}
    return render(request,'rentals/delete_rental.html',context)

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def generatePayment(request, id):
    rental = Rental.objects.get(rental_id=id)
    yearRental = rental.get_year_rental()
    monthRental = rental.get_month_rental()
    dayRental = rental.get_day_rental()
    rentals =  Rental.objects.all()
    customers = Customer.objects.all()
    staffList = Staff.objects.all()
    return render(request,'rentals/payment_form.html',{'rentals':rentals,'customers':customers,'staffList':staffList,'rental':rental,'yearRental':yearRental,'monthRental':monthRental,'dayRental':dayRental})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def addNewPayment(request):
    #rental = Rental.objects.get(rental_id=id)
    rentals = Rental.objects.all()
    customers = Customer.objects.all()
    staffList = Staff.objects.all()
    form = PaymentForm(request.POST,request.FILES) 
    
    if form.is_valid():
        form.save()
        return redirect("payments")
    return render(request,'rentals/payment_form.html',{'form':form,'rentals':rentals,'customers':customers,'staffList':staffList})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def editPayment(request,id):
    rentals = Rental.objects.all()
    customers = Customer.objects.all()
    staffList = Staff.objects.all()
    payment = Payment.objects.get(payment_id=id)
    yearPayment = payment.get_year_payment()
    monthPayment = payment.get_month_payment()
    dayPayment = payment.get_day_payment()

    return render(request,'rentals/payment_form_update.html', {'payment':payment,'rentals':rentals,'customers':customers,'staffList':staffList,'yearPayment':yearPayment,'monthPayment':monthPayment,'dayPayment':dayPayment})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def updatePayment(request,id):

    rentals = Rental.objects.all()
    customers = Customer.objects.all()
    staffList = Staff.objects.all()
    payment = Payment.objects.get(payment_id=id)
    try:
        yearPayment = payment.get_year_payment()
        monthPayment = payment.get_month_payment()
        dayPayment = payment.get_day_payment()
    except AttributeError:
        yearPayment = "2021"
        monthPayment = "04"
        dayPayment = "30"    

    form = PaymentForm(request.POST,request.FILES, instance = payment)  
    if form.is_valid():  
        form.save()  
        return redirect("payments")  

    return render(request,'rentals/payment_form_update.html', {'payment':payment,'rentals':rentals,'customers':customers,'staffList':staffList,'yearPayment':yearPayment,'monthPayment':monthPayment,'dayPayment':dayPayment})

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def deletePayment(request, id):  
    payment = Payment.objects.get(payment_id=id)
    if request.method == "POST":
        payment.delete()  
        return redirect("payments")
    context = {'item':payment}
    return render(request,'rentals/delete_payment.html',context)

#vistas reportes
class RentalsListView(ListView):
    model = Rental
    template_name = 'rentals/rental_report_template.html'

@allowed_users(allowed_roles=['admin','manager','employee'])
@login_required(login_url='login')
def rentals_render_pdf_view(request,*args, **kwargs):
    pk = kwargs.get('pk')
    rental = get_object_or_404(Rental,pk=pk)

    template_path = 'rentals/pdf2.html'
    context = {'rental': rental}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download:
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    #if display:
    response['Content-Disposition'] = 'filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@allowed_users(allowed_roles=['admin','manager','employee'])            
@login_required(login_url='login')
def render_pdf_view(request):
    template_path = 'rentals/pdf1.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download:
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    #if display:
    response['Content-Disposition'] = 'filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    