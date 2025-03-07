from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Veiculo
from .forms import VeiculoForm

def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'tarefas/lista_veiculos.html', {'veiculos': veiculos})

def adicionar_veiculo(request):
    if request.method == "POST":
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_veiculos')
    else:
        form = VeiculoForm()
    return render(request, 'tarefas/adicionar_veiculo.html', {'form': form})

def lista_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'tarefas/lista_servicos.html', {'servicos': servicos})

def adicionar_servico(request):
    if request.method == "POST":
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_servicos')
    else:
        form = ServicoForm()
    return render(request, 'tarefas/adicionar_servico.html', {'form': form})

