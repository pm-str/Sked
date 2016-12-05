from django import forms
from .models import Task


FORM_ATTRS = {'class': 'form-control'}


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'date', 'start', 'end', 'date_notice', 'time_notice', 'repeat', 'color')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'date': forms.DateInput(attrs={'class': 'input-calendar form-control', 'placeholder': 'Date'}),
            'start': forms.TimeInput(attrs={'class': 'form-control time', 'placeholder': 'Start time'}),
            'end': forms.TimeInput(attrs={'class': 'form-control time', 'placeholder': 'End time'}),
            'time_notice': forms.TimeInput(attrs={'class': 'form-control time', 'placeholder': 'Time notice'}),
            'date_notice': forms.DateInput(
                attrs={'class': 'input-calendar form-control', 'placeholder': 'Date notice'}),
            'repeat': forms.Select(attrs=FORM_ATTRS),
            'color': forms.Select(attrs=FORM_ATTRS)
        }