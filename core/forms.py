from django import forms
from .models import Presenca, Professor

class CadastroPresencaForm(forms.ModelForm):
    nome_professor = forms.ModelChoiceField(queryset=Professor.objects.all())

    class Meta:
        model = Presenca
        fields = ['nome_aluno', 'nome_professor']
