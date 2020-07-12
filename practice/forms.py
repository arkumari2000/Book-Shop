from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreate(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class OrderUpdate(ModelForm):
    class Meta:
        model = Order
        fields = ['status']


class BookUpdate(ModelForm):
    class Meta:
        model = Product
        fields = ['Price']


class AddBook(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class NewCustomer(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class ProfileUpdate(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
