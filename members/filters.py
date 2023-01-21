import django_filters
from django_filters import DateFilter

from .models import *

class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['contact','email','id','salary']
    
