from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from devices.models import Lamp, LampStatistics
from devices.forms import LampForm
from decimal import Decimal
from django.utils import timezone
from django.db import transaction


@csrf_exempt
def toggle_lamp(request, lamp_id):
    lamp = get_object_or_404(Lamp, id=lamp_id)
    new_status = request.POST.get('status')
    lamp.status = new_status
    lamp.save()
    return JsonResponse({'success': True})


@csrf_exempt
@transaction.atomic
def update_brightness(request, lamp_id):
    lamp = get_object_or_404(Lamp, id=lamp_id)
    new_brightness = request.POST.get('brightness')
    lamp.brightness = new_brightness
    lamp.save()
    return JsonResponse({'success': True})


@csrf_exempt
@transaction.atomic
def update_color(request, lamp_id):
    lamp = get_object_or_404(Lamp, id=lamp_id)
    new_color = request.POST.get('color')
    lamp.color = new_color
    lamp.save()

    return JsonResponse({'success': True})


def index(request):
    lamps = Lamp.objects.filter(user=request.user)

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


def create_lamp(request):
    if request.method == 'POST':
        form = LampForm(request.POST)
        if form.is_valid():
            # Speichern Sie das Modell, wenn das Formular gültig ist
            lamp = form.save(commit=False)
            lamp.user = request.user  # Setzen Sie den Benutzer auf den aktuellen Benutzer
            lamp.save()

            LampStatistics.create_statistics(lamp)
            return redirect('main:index')  # Hier 'lamp_list' durch den Namen Ihrer Lampenliste ersetzen
    else:
        form = LampForm()

    context = {
        'title': 'Lampe hinzufügen',
        'form': form,
    }
    return render(request, 'devices/create_lamp.html', context)


def base(request):
    return render(request, 'main/base.html')