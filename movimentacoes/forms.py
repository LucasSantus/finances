from django import forms
from django.forms import fields
from movimentacoes.models import Movimentacao

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ("__all__")