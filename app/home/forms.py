from django import forms
from .models import Task


FORM_ATTRS = {'class': 'form-control'}


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'date', 'start', 'end', 'date_notice', 'time_notice', 'repeat', 'color')
        widgets = {
            'name': forms.TextInput(attrs=FORM_ATTRS),
            'description': forms.Textarea(attrs=FORM_ATTRS),
            'date': forms.DateInput(attrs={'class': 'input-calendar form-control'}),
            'start': forms.TimeInput(attrs={'class': 'form-control time'}),
            'end': forms.TimeInput(attrs={'class': 'form-control time'}),
            'time_notice': forms.TimeInput(attrs={'class': 'form-control time'}),
            'date_notice': forms.DateInput(attrs={'class': 'input-calendar form-control'}),
            'repeat': forms.Select(attrs=FORM_ATTRS),
            'color': forms.Select(attrs=FORM_ATTRS)
        }