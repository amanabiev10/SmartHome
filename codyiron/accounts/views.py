from django.shortcuts import render, redirect
from accounts.forms import UserRegistrationForm, UserLoginForm
from django.contrib import auth, messages
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from devices.permissions import LampPermissions


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
            else:
                messages.error(request, 'Ungültiger Benutzername oder Passwort!')
    else:
        form = UserLoginForm()

    context = {
        'title': 'Anmelden',
        'form': form
    }

    return render(request, 'accounts/login.html', context)


def registration(request):

    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            add_permissions = LampPermissions()
            add_permissions.assign_create_lamp_permission(user)
            add_permissions.assign_change_lamp_permission(user)
            add_permissions.assign_view_lamp_permission(user)
            add_permissions.assign_delete_lamp_permission(user)
            messages.success(request, 'Herzlichen Glückwunsch, Sie haben erfolgreich registriert.!')
            # Weiterleitung zur Anmeldeseite
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'accounts',
        'form': form
    }

    return render(request, 'accounts/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))