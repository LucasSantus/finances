from django.shortcuts import redirect, render
from movimentacoes.forms import MovimentacaoForm

def criar_movimentacao(request):
    form = MovimentacaoForm()
    
    if request.method == "POST":
        form = MovimentacaoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("index")
            
    context = {
        'form': form
    }
    return render(request, "criar_movimentacao.html", context)