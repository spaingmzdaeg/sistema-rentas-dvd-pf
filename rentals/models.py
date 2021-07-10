from django.db import models
from addresses.models import Address
from films.models import Film
from django_resized import ResizedImageField
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    customer_id = models.AutoField(primary_key=True)
    store = models.ForeignKey('Store',null=True,blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    profile_pic = ResizedImageField(size=[139, 156], default="userv2.png",upload_to='customerpics', blank=True, null=True)
    #profile_pic = models.ImageField(default="user.png",null=True,blank=True,upload_to='customerpics')
    address = models.ForeignKey(Address,null=True,blank=True,on_delete=models.CASCADE)
    activebool = models.BooleanField(default=True)
    create_date = models.DateField(auto_now=True)
    last_update = models.DateTimeField(auto_now=True)
    active = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.first_name+'-'+self.last_name+'-'+str(self.address)

    class Meta:
        db_table = 'customer'

class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film,on_delete=models.CASCADE)
    store = models.ForeignKey('Store',on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.inventory_id)+'-'+str(self.film)+'-'+str(self.store)

    class Meta:
        db_table = 'inventory'

class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateField()
    inventory = models.ForeignKey(Inventory,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    return_date = models.DateTimeField(blank=True,null=True)
    staff = models.ForeignKey('Staff',on_delete=models.CASCADE)
    last_update = models.DateField(auto_now=True)

    def get_year_rental(self):
        return self.rental_date.strftime('%Y')

    def get_month_rental(self):
        return self.rental_date.strftime('%m')

    def get_day_rental(self):
        return self.rental_date.strftime('%d')

    def get_year_return(self):
        try:
            return self.return_date.strftime('%Y')
        except AttributeError:
            return ""    

    def get_month_return(self):
        try:
            return self.return_date.strftime('%m')
        except AttributeError:
            return ""    

    def get_day_return(self):
        try:
            return self.return_date.strftime('%d')
        except AttributeError:
            return ""             

    def __str__(self):
        return str(self.rental_id)+'-'+str(self.inventory)+'-'+str(self.customer)+'-'+str(self.staff)


    class Meta:
        db_table = 'rental'

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    staff = models.ForeignKey('Staff',on_delete=models.CASCADE)
    rental = models.ForeignKey('Rental',on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()

    def get_year_payment(self):
        return self.payment_date.strftime('%Y')

    def get_month_payment(self):
        return self.payment_date.strftime('%m')

    def get_day_payment(self):
        return self.payment_date.strftime('%d')  

    def __str__(self):
        return str(self.payment_id)


    class Meta:
        db_table = 'payment'

class Staff(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    email = models.EmailField()
    store = models.ForeignKey('Store',on_delete=models.CASCADE)
    active =  models.BooleanField()
    last_update = models.DateTimeField(auto_now=True)
    picture = ResizedImageField(size=[139, 156], default="userv2.png",upload_to='staffpics', blank=True, null=True)

    def __str__(self):
        return self.first_name+' '+self.last_name+'-'+str(self.address)

    class Meta:
        db_table = 'staff'
        
#siempre tiene que exister un store y un staff uno a uno obligatorio
class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.OneToOneField(
       Staff,  related_name='store_managed_by_me',on_delete=models.CASCADE
    )
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.store_id) + '-' + str(self.address)
    
    class Meta:
        db_table = 'store'     

            


                   
                
    
