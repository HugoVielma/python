from dataclasses import fields
import email
from django import forms
from . models import Profesor


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email']
