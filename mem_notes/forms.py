from django import forms
from location_field.forms.plain import PlainLocationField

from mem_notes.models import Memories


class RememberForm(forms.ModelForm):
    class Meta:
        model = Memories
        fields = ['subject', 'description', 'city', 'location']
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': 'Тема',}),
            'description': forms.Textarea(attrs={'placeholder': 'Как можно подробнее..', }),
            'city': forms.TextInput(attrs={'placeholder': 'Город, улицу и номер дома', }),
            'location': forms.HiddenInput(attrs={'placeholder': 'Тут ничего не нужно'}),
        }

