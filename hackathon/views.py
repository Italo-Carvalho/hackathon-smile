import decimal

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .form import *
from .models import *


def ViagemView(request):
    estados = Estado.objects.all()
    if request.method == 'POST':
        form = ViagemForm(request.POST)
        if form.is_valid():
            viagem = form.save()
            return HttpResponseRedirect(f'viajem/{viagem.pk}')
        else:
            form = ViagemForm()
    else:
        form = ViagemForm()

    return render(request, 'index.html', {'form': form, 'estados': estados})


def ViagemEX(request, pk):
    viagem = get_object_or_404(Viagem, pk=pk)
    atividade = Atividade.objects.filter(lugar=viagem.lugar.pk).all()
    hospedagem = Hospedagem.objects.filter(lugar=viagem.lugar.pk).all()
    restaurante = Restaurante.objects.filter(lugar=viagem.lugar.pk).all()

    if request.method == 'POST':
        form = ExtrasForm(request.POST)
        if form.is_valid():
            resultado = form.save()

            return redirect('resultado', pk=resultado.pk)
        else:
            form = ExtrasForm()
    else:
        form = ExtrasForm()

    context = {
        'viagem': viagem,
        'form': form,
        'atividade': atividade,
        'hospedagem': hospedagem,
        'restaurante': restaurante,
    }
    return render(request, 'viagem1.html', context)


def Resultado(request, pk):
    extras = get_object_or_404(Extras, pk=pk)
    milhas = decimal.Decimal(14.28570)
    milhas_mes = extras.viagem.porcentagem * milhas
    total = extras.viagem.lugar.preco + extras.ativadade.preco + \
        extras.hospedagem.preco + extras.restaurante.preco
    milhas_total = total * milhas
    meses = total / extras.viagem.porcentagem

    context = {
        'dados': extras,
        'total': total,
        'meses': meses,
        'milhas_mes': milhas_mes,
        'milhas_total': milhas_total,
    }
    return render(request, 'resultado.html', context)


def load_locais(request):
    estado_id = request.GET.get('estado')
    locais = Lugar.objects.filter(estado_id=estado_id).order_by('nome')
    # ------------
    lugar_id = request.GET.get('lugar')
    hospedagens = Hospedagem.objects.filter(lugar_id=lugar_id).order_by('nome')
    context = {
        'locais': locais,
        'hospedagens': hospedagens
    }
    return render(request, 'lugar.html', context)
