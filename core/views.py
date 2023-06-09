from django.shortcuts import render, redirect
from .models import Presenca
from .forms import CadastroPresencaForm

def cadastrar_presenca(request):
    if request.method == 'POST':
        form = CadastroPresencaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'cadastro_presenca.html', {'form': form, 'success_message': 'Presença cadastrada com sucesso.'})
    else:
        form = CadastroPresencaForm()

    return render(request, 'cadastro_presenca.html', {'form': form})


def listar_presenca(request):
    presencas = Presenca.objects.all()
    return render(request, 'listar_presenca.html', {'presencas': presencas})
