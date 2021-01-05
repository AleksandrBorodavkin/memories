from django import forms
from location_field.forms.plain import PlainLocationField

from mem_notes.models import Memories


class RememberForm(forms.ModelForm):
    class Meta:
        model = Memories
        fields = ['subject', 'description', 'city', 'location']
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': 'Тема',
                                              'class': 'm-1 form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Как можно подробнее..',
                                                 'class': 'm-1 form-control' }),
            'city': forms.TextInput(attrs={'placeholder': 'Город, улицу и номер дома',
                                           'class': 'm-1 form-control'}),
            'location': forms.HiddenInput(attrs={'placeholder': 'Тут ничего не нужно',
                                                 'class': 'm-1 form-control'}),
        }

