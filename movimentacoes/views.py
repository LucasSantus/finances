from django.shortcuts import render
from movimentacoes.forms import MovimentacaoForm

def criar_movimentacao(request):
    form = MovimentacaoForm()
    context = {
        'form': form
    }
    return render(request, "criar_movimentacao.html", context)