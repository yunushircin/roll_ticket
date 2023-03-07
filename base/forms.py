from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms

class ProblemForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset= Category.objects.all(),
        empty_label='Kategori Seç',
        label='Kategori Seç'
    )

    user = forms.ModelChoiceField(
        queryset= User.objects.all(),
        empty_label='M.Temsilcisi',
        label='M.Temsilcisi'
    )
    class Meta:
        model = Problem
        fields = ['customer_name', 'category', 'user', 'description', 'status']
        widgets = {
            'customer_name': forms.TextInput(attrs={'placeholder': 'Kullanıcı Adı'}),
            'description': forms.TextInput(attrs={'placeholder': 'Açıklama gir'}),
        }
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Yeni Kategori Giriniz'}),
        }

class AddUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Şifre'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Şifre Doğrula'}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Kullanıcı Adı'}),
        }
