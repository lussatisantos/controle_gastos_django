from .models import Transacao
from django.forms import ModelForm

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'observacoes', 'categoria']
