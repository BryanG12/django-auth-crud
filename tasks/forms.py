from django import forms
from .models import Task


class TaskForm (forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        labels = {
            'title': 'Titulo',
            'description': 'Descripción',
            'important': 'Importante?'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el titulo'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe la description'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }
