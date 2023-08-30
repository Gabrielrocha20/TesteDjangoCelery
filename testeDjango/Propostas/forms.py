# forms.py

from django import forms
from dynamic_form_fields.forms import DynamicFormFieldFormMixin

from .models import PropostaAceita


class PropostaAceitaForm(DynamicFormFieldFormMixin, forms.ModelForm):
    class Meta:
        model = PropostaAceita
        fields = ['nome']
