from django import forms

from .models import Word


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ('name', 'translation', 'transcription', 'example')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'transcription': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Transcription'}),
            'translation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Translation'}),
            'example': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example'}),
        }
