from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from accounts.models import User


class UserRegistrationForm(UserCreationForm):

    fields = '__all__'

    # Feld für den Vornamen des Benutzers
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'first_name',
        'name': 'first_name',
        'class': 'form-control form-control-lg',
        'placeholder': 'Vorname angeben',
    }))

    # Feld für den Nachnamen des Benutzers
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'last_name',
        'name': 'last_name',
        'class': 'form-control form-control-lg',
        'placeholder': 'Nachname angeben',
    }))

    # Feld für den Benutzernamen
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'username',
        'name': 'username',
        'class': 'form-control form-control-lg',
        'placeholder': 'Benutzername angeben',
    }))

    # Feld für die E-Mail-Adresse
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'type': 'email',
        'id': 'email',
        'name': 'email',
        'class': 'form-control form-control-lg',
        'placeholder': 'E-Mail angeben'
    }))

    # Feld für das Passwort
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': 'password',
        'id': 'password1',
        'name': 'password1',
        'class': 'form-control form-control-lg',
        'placeholder': 'Passwort angeben'
    }))

    # Feld zur Bestätigung des Passworts
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': 'password',
        'id': 'password2',
        'name': 'password2',
        'class': 'form-control form-control-lg',
        'placeholder': 'Passwort wiederholen'
    }))

    class Meta:
        # Verknüpfung des Formulars mit dem User-Modell
        model = User
        # Die Felder, die im Formular angezeigt und bearbeitet werden sollen
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'username',
        'name': 'username',
        'class': 'input100',
        'placeholder': 'Benutzername angeben',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': 'password',
        'id': 'password',
        'name': 'password',
        'class': 'input100',
        'placeholder': 'Passwort angeben'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')