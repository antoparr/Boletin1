from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import TuFormulario


def tu_vista(request):
    if request.method == 'POST':
        form = TuFormulario(request.POST)
        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            dias_semana = form.cleaned_data['dias_semana']
            correo_electronico = form.cleaned_data['correo_electronico']

            print(f"Fecha de inicio: {fecha_inicio}")
            print(f"Fecha fin: {fecha_fin}")
            print(f"Días de la semana: {dias_semana}")
            print(f"Correo electrónico: {correo_electronico}")

    else:
        form = TuFormulario()

    return render(request, 'formularios.html', {'form': form})