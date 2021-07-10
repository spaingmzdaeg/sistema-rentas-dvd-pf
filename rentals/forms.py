from django import forms
from .models import Staff,Store,Customer,Inventory,Film,Rental,Payment


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name','last_name','address','email','store','active','picture']

    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)

        # sets the placeholder key/value in the attrs for a widget
        # when the form is instantiated (so the widget already exists)
        self.fields['first_name'].widget.attrs['placeholder'] = 'ingrese nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'insert apellido'
        self.fields['email'].widget.attrs['placeholder'] = 'ingrese email'
        

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['manager_staff','address']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['store','first_name','last_name','email','profile_pic','address','activebool','active']

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)

        # sets the placeholder key/value in the attrs for a widget
        # when the form is instantiated (so the widget already exists)
        self.fields['first_name'].widget.attrs['placeholder'] = 'ingrese nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'ingrese apellido'
        self.fields['email'].widget.attrs['placeholder'] = 'ingrese email'
           
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['film','store']

class DateInput(forms.DateInput):
    input_type = 'date'

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['rental_date','inventory','customer','return_date','staff']
        widgets = {
            'rental_date': DateInput(),
            'return_date':DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(RentalForm, self).__init__(*args, **kwargs)

        # sets the placeholder key/value in the attrs for a widget
        # when the form is instantiated (so the widget already exists)
        self.fields['rental_date'].widget.attrs['placeholder'] = 'aa-mm-dd'
        self.fields['return_date'].widget.attrs['placeholder'] = 'aa-mm-dd'
         

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['customer','staff','rental','amount','payment_date']
        widgets = {
            'payment_date':DateInput()
        }         


                           





       