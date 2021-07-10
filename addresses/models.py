from django.db import models

# Create your models here.
class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50,blank=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey('City',on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=10,blank=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.address + '-' + self.address2 + '-' + str(self.city)

    class Meta:
        db_table='address'

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey('Country',on_delete=models.CASCADE)
    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.city + '-' + str(self.country)

    class Meta:
        db_table = 'city'

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.country

    class Meta:
        db_table = 'country'    


                
    

            

