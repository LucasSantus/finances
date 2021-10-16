from django.shortcuts import render
from movimentacoes.models import Movimentacao, Tipo
from contas.models import Conta

from datetime import datetime
from django.db.models import Sum

def index(request):
    movimentacoes = Movimentacao.objects.order_by('-data')
    
    mes_atual = datetime.now().month
    
    total_receitas = movimentacoes.filter(
        tipo = Tipo.RECEITA,
        data__month = mes_atual
    ).aggregate(total = Sum('valor'))['total']

    total_despesas = movimentacoes.filter(
        tipo = Tipo.DESPESA,
        data__month = mes_atual
    )
    
    ultimas_movimentacoes = movimentacoes[:4]
    
    conta = Conta.objects.first()

    context = {
        'saldo_em_conta': conta.saldo,
        'ultimas_movimentacoes': ultimas_movimentacoes,
        'total_receitas': total_receitas,
        'total_despesas': total_despesas
    }
    
    return render(request, "index.html", context)