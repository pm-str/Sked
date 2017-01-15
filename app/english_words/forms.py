from django import forms

from .models import Word


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ('name', 'transcription', 'translation', 'example')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Word'}),
            'transcription': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '[ transcription ]'}),
            'translation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Translation'}),
            'example': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example ... '}),
        }
