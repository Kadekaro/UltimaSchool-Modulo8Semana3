from datetime import datetime, timedelta

from django import forms
from Base.models import Contato


class contatoForms(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']

