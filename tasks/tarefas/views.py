from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Veiculo, Servico
from .forms import ClienteForm, VeiculoForm, ServicoForm

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'tarefas/lista_clientes.html', {'clientes': clientes})

def detalhes_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'tarefas/detalhes_cliente.html', {'cliente': cliente})

def adicionar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'tarefas/adicionar_cliente.html', {'form': form})
