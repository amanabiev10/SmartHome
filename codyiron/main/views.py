from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from devices.models import Lamp
from devices.forms import LampForm


def create_lamp(request):
    if request.method == 'POST':
        form = LampForm(request.POST)
        if form.is_valid():
            # Speichern Sie das Modell, wenn das Formular gültig ist
            lamp = form.save(commit=False)
            lamp.user = request.user  # Setzen Sie den Benutzer auf den aktuellen Benutzer
            lamp.save()
            return redirect('lamp_list')  # Hier 'lamp_list' durch den Namen Ihrer Lampenliste ersetzen
    else:
        form = LampForm()

    context = {
        'title': 'Lampe hinzufügen',
        'form': form,
    }
    return render(request, 'devices/create_lamp.html', context)


def update_lamp(request, lamp_id):
    lamp = get_object_or_404(Lamp, id=lamp_id, user=request.user)

    if request.method == 'POST':
        form = LampForm(request.POST, instance=lamp)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = LampForm(instance=lamp)

    context = {
        'title': f'Update Lampe: {lamp.name}',
        'form': form,
    }
    return render(request, 'devices/update_lamp.html', context)


def index(request):
    lamps = Lamp.objects.all()

    # Konvertiere die Zeitplandaten in das richtige Format (HH:MM)
    for lamp in lamps:
        if lamp.schedule_on:
            lamp.schedule_on = lamp.schedule_on.strftime('%H:%M')
        if lamp.schedule_off:
            lamp.schedule_off = lamp.schedule_off.strftime('%H:%M')

    context = {
        'title': 'Lampensteuerung',
        'lamps': lamps
    }

    return render(request, 'main/index.html', context)


def base(request):
    return render(request, 'main/base.html')