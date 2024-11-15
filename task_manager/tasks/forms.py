from django import forms
from .models import Task
from django.forms.widgets import DateInput

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'deadline', 'priority']
        widgets = {
            'deadline': DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'YYYY-MM-DD'}),
        }
