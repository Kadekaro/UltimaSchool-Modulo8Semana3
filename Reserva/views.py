from django.shortcuts import render
from Reserva.forms import ReservaForm
from Reserva.models import Reserva


# Create your views here.

def reserva(request):
    form = ReservaForm(request.POST or None)
    sucesso = False
    if form.is_valid():
        form.save()
        sucesso = True
    cont = {'form': form,
            'sucesso': sucesso}

    return render(request, "reserva.html", cont)
