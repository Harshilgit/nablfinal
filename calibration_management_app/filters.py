from django.contrib.auth.models import User
import django_filters
from .models import *
from .forms import *


class DateInput(forms.DateInput):
    input_type = 'date'


class TodoFilter(django_filters.FilterSet):
    task_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Todo
        fields = ['task_name', 'priority', 'created_at', 'assigned_to',]
        
