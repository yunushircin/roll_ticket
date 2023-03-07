import django_filters
from django import forms

from .models import *

class ProblemFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='date_created', lookup_expr='gte',
                            widget=forms.TextInput(attrs={'id': 'datepickerstart', 'placeholder':'Başlangıç Tarihi'}))
    end_date = django_filters.DateFilter(field_name='date_created', lookup_expr='lte',
                          widget=forms.TextInput(attrs={'id': 'datepickerend', 'placeholder':'Bitiş Tarihi'}))
    customer_name = django_filters.CharFilter(field_name='customer_name', lookup_expr='icontains',
                      widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı'}))
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), empty_label='Kategori Seç', 
                                 widget=forms.Select(attrs={'placeholder': 'Kategori Seç...'}))
    user = django_filters.ModelChoiceFilter(queryset=User.objects.all(), empty_label='Personel Seç', 
                                 widget=forms.Select(attrs={'placeholder': 'Personel Seç...'}))
    # status = ModelChoiceFilter(queryset=Problem.objects.values_list('status', flat=True).distinct(), empty_label='Durum', 
    #                               widget=forms.Select(attrs={'placeholder': 'Durum Seç...'}))

    status = django_filters.ChoiceFilter(choices=Problem.STATUS, empty_label='Durum Seç')
    
    
    
    class Meta:
        model = Problem
        fields = '__all__'
        exclude = ['date_created', 'customer_name']
