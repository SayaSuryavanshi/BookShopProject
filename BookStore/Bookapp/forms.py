from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customers, Products

class Registerform(UserCreationForm):
    password1=forms.CharField(label="Enter Password ", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Confirm Password ", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

        labels={
            'username':'Enter Username ',
            'first_name':'Enter First Name  ',
            'last_name':'Enter Last Name ',
            'email':'Enter Email ',
        }

        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username=forms.CharField(label="Enter Username ", widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label="Enter Password ", widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=['username','password']

class CustomersForm(forms.ModelForm):
    class Meta:
        model=Customers
        fields=['custname','custaddress','city','state','custcontact','pincode']

        labels={
            'custname':'Enter Custname ',
            'custaddress':'Enter Address  ',
            'city':'Enter City ',
            'state':'Select State ',
            'custcontact':'Enter Contact ',
            'pincode':'Enter pincode ',
        }

        widgets={
            'custname':forms.TextInput(attrs={'class':'form-control'}),
            'custaddress':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'custcontact':forms.TextInput(attrs={'class':'form-control'}),
            'pincode':forms.TextInput(attrs={'class':'form-control'}),
        }

#For Admin Panel
class ProductsForm(forms.ModelForm):
    class Meta:
        model=Products
        fields=['prodname','proddesc','prodprice','prodrating','prodimage','cat']

        labels={
            'prodname':'Enter Product name ',
            'proddesc':'Enter Description  ',
            'prodprice':'Enter Price ',
            'prodrating':'Enter Rating ',
            'prodimage':'Enter Image ',
            'cat':'Select Category ',
        }

        widgets={
            'prodname':forms.TextInput(attrs={'class':'form-control'}),
            'proddesc':forms.TextInput(attrs={'class':'form-control'}),
            'prodprice':forms.TextInput(attrs={'class':'form-control'}),
            'prodrating':forms.TextInput(attrs={'class':'form-control'}),
            'prodimage':forms.FileInput(attrs={'class':'form-control'}),
            'cat':forms.Select(attrs={'class':'form-control'}),
        }

        def clean_prodName(self):
            prodName=self.cleaned.data.get('prodname')
            if not prodName.isalpha():
                raise forms.ValidationError('Product name must contain only alphabets.')
            return prodName

