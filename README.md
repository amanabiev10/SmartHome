# Smart Home Control Web App Dokumentation

## Inhaltsverzeichnis
1. [Funktionalitäten](#funktionalitäten)
2. [Technologien](#technologien)
3. [Installation](#installation)
4. [Django Accounts App Dokumentation](#django-accounts-app-dokumentation)
5. [Django Devices App Dokumentation](#django-devices-app-dokumentation)
6. [Django Main App Dokumentation](#django-main-app-dokumentation)
6. [API-Dokumentation](#api-dokumentation)
7. [Beispielcode ESP32](#beispielcode-esp32)


## Funktionalitäten
Das Projekt ermöglicht es Benutzern, Geräte in ihrem Smart Home über eine Webseite zu steuern. Derzeit unterstützt die Anwendung die Steuerung von Lampen mithilfe von ESP32-Mikrocontrollern. Die Hauptfunktionen umfassen:

- An/Ausschalten von Lampen
- Verwalten der Helligkeit von Lampen
- Ändern der Farben von Lampen

Benutzer können über die Webseite Geräte hinzufügen, ein Konto erstellen und API-Token generieren, um die Geräte zu steuern.

## Technologien
Das Projekt nutzt folgende Technologien:

- Frontend: HTML, CSS, JavaScript
- Backend: [Python, Django, Django REST framework]
- ESP32 Programmierung: [C++, Python (Was Sie lieben)]

## Installation
Um das Projekt lokal auszuführen, führen Sie die folgenden Schritte aus:

1. Klone das Repository: `git clone https://github.com/amanabiev10/Hausmesse.git`
2. Wechsle in das Verzeichnis: `cd dein-projekt`
3. Installiere die Abhängigkeiten: [Befehl zur Installation von Abhängigkeiten, z.B., npm install]

# Django Accounts App Dokumentation

Die `accounts`-App in Ihrem Django-Projekt enthält Benutzermodelle, Formulare für die Benutzerregistrierung und -anmeldung sowie Ansichten für diese Aktionen. Hier ist eine Dokumentation für die Klassen und Methoden in der `accounts`-App.

## models.py

### User(AbstractUser)

Die `User`-Klasse erweitert das integrierte Django-Benutzermodell `AbstractUser` und enthält zusätzliche Felder.

- `display_name`: Ein Zeichenfeld für den Anzeigenamen des Benutzers.
- `registered`: Ein `DateTimeField`, das den Zeitpunkt der Registrierung des Benutzers aufzeichnet.
- `created_at`: Ein `DateTimeField`, das den Zeitpunkt der letzten Aktualisierung des Benutzerprofils aufzeichnet.

#### Methoden

- `save(self, *args, **kwargs)`: Überschreibt die Standard-Save-Methode, um den Anzeigenamen des Benutzers automatisch aus dem Vornamen und Nachnamen zu generieren.
- `__str__(self)`: Gibt eine lesbare Zeichenfolgendarstellung des Benutzers zurück.

#### Meta

Enthält Meta-Informationen wie den Anzeigenamen für die Admin-Oberfläche.

## forms.py

### UserRegistrationForm(UserCreationForm)

Das `UserRegistrationForm` erbt von Django `UserCreationForm` und fügt zusätzliche Felder für die Benutzerregistrierung hinzu.

#### Meta

- `model`: Verknüpft das Formular mit dem `User`-Modell.
- `fields`: Gibt die im Formular anzuzeigenden und zu bearbeitenden Felder an.

## views.py

### login(request)

Die Ansicht für die Benutzeranmeldung.

- **POST**: Überprüft die Eingabedaten, authentifiziert den Benutzer und leitet ihn zur Hauptseite weiter. Bei ungültigen Anmeldeinformationen wird eine Fehlermeldung angezeigt.
- **GET**: Zeigt das Anmeldeformular an.

### registration(request)

Die Ansicht für die Benutzerregistrierung.

- **POST**: Überprüft die Eingabedaten, erstellt einen neuen Benutzer, weist Lampenberechtigungen zu und leitet zur Anmeldeseite weiter.
- **GET**: Zeigt das Registrierungsformular an.

### logout(request)

Die Ansicht für die Benutzerabmeldung.

- Loggt den Benutzer aus und leitet zur Hauptseite weiter.

# Django Devices App Dokumentation

Die `devices`-App in Ihrem Django-Projekt enthält Modelle für Lampen, Ansichten für die Steuerung von Lampen, Berechtigungen und Serialisierer für die API. Hier ist eine Dokumentation für die Klassen und Methoden in der `devices`-App.

## models.py

### Lamp(models.Model)

Die `Lamp`-Klasse repräsentiert eine Lampe im Smart Home.

- `user`: Fremdschlüssel zum Benutzer, dem die Lampe gehört.
- `name`: Der Name der Lampe.
- `status`: Der Status der Lampe (An/Aus).
- `color`: Die Farbe der Lampe.
- `brightness`: Die Helligkeit der Lampe (0-100).
- `schedule_on`: Die Zeit, zu der die Lampe eingeschaltet wird (optional).
- `schedule_off`: Die Zeit, zu der die Lampe ausgeschaltet wird (optional).
- `created_at`: Das Datum und die Uhrzeit, zu denen die Lampe erstellt wurde.

#### Methoden

- `calculate_energy_consumption()`: Berechnet den Energieverbrauch der Lampe basierend auf Helligkeit.
- `save(self, *args, **kwargs)`: Überschreibt die Standard-Save-Methode, um die Lampenstatistik zu aktualisieren.

### LampStatistics(models.Model)

Die `LampStatistics`-Klasse enthält Statistiken für den Energieverbrauch und die Nutzungsdauer einer Lampe.

- `lamp`: Fremdschlüssel zur zugehörigen Lampe.
- `timestamp`: Das Datum und die Uhrzeit der Statistik.
- `energy_consumption`: Der Energieverbrauch der Lampe.
- `usage_duration`: Die Nutzungsdauer der Lampe.

#### Methoden

- `create_statistics(lamp)`: Erstellt eine neue Statistik für die gegebene Lampe.

## permissions.py

### LampPermissions

Die `LampPermissions`-Klasse enthält Methoden zum Zuweisen von Berechtigungen für Lampenaktionen.

- `assign_create_lamp_permission(user)`: Weist dem Benutzer die Berechtigung zum Erstellen einer Lampe zu.
- `assign_view_lamp_permission(user)`: Weist dem Benutzer die Berechtigung zum Anzeigen einer Lampe zu.
- `assign_change_lamp_permission(user)`: Weist dem Benutzer die Berechtigung zum Ändern einer Lampe zu.
- `assign_delete_lamp_permission(user)`: Weist dem Benutzer die Berechtigung zum Löschen einer Lampe zu.

## serializers.py

### LampSerializer(serializers.ModelSerializer)

Der `LampSerializer` serialisiert Lampenmodelle für die Verwendung in der API.

## forms.py

### LampForm(forms.ModelForm)

Das `LampForm` definiert ein Formular für die Eingabe von Lampendaten.

## urls.py

### urlpatterns

Die `urlpatterns` definiert die URL-Muster für die `devices`-App.

## views.py

### api_token_list(request)

Die Ansicht zeigt die API-Token des angemeldeten Benutzers an.

### TokenHasReadWriteScope(BasePermission)

Eine benutzerdefinierte Berechtigungsklasse, die sicherstellt, dass das Token des Benutzers die erforderlichen Berechtigungen hat.

### LampList(generics.ListCreateAPIView)

Eine API-Ansicht für das Auflisten und Erstellen von Lampen.

### LampDetail(generics.RetrieveUpdateDestroyAPIView)

Eine API-Ansicht für das Abrufen, Aktualisieren und Löschen von Lampen.

### generate_api_token(request)

Die Ansicht generiert ein API-Token für den angemeldeten Benutzer.

# Django Main App Dokumentation

Die `main`-App in Ihrem Django-Projekt enthält Ansichten und URLs für die Hauptseite, die Steuerung von Lampen und das Hinzufügen von Lampen. Hier ist eine Dokumentation für die Klassen und Methoden in der `main`-App.

## urls.py

### urlpatterns

Die `urlpatterns` definiert die URL-Muster für die `main`-App.

- `index`: Die Hauptseite, auf der die Lampensteuerung angezeigt wird.
- `create_lamp`: Die Seite zum Hinzufügen einer neuen Lampe.
- `toggle_lamp/<int:lamp_id>/`: Die URL zum Umschalten des Status einer Lampe.
- `update_brightness/<int:lamp_id>/`: Die URL zum Aktualisieren der Helligkeit einer Lampe.
- `update_color/<int:lamp_id>/`: Die URL zum Aktualisieren der Farbe einer Lampe.

## views.py

### toggle_lamp(request, lamp_id)

Eine Ansicht zum Umschalten des Status einer Lampe.

- **POST**: Nimmt einen POST-Parameter für den neuen Status entgegen und aktualisiert den Status der Lampe.

### update_brightness(request, lamp_id)

Eine Ansicht zum Aktualisieren der Helligkeit einer Lampe.

- **POST**: Nimmt einen POST-Parameter für die neue Helligkeit entgegen und aktualisiert die Helligkeit der Lampe.

### update_color(request, lamp_id)

Eine Ansicht zum Aktualisieren der Farbe einer Lampe.

- **POST**: Nimmt einen POST-Parameter für die neue Farbe entgegen und aktualisiert die Farbe der Lampe.

### index(request)

Die Hauptansicht der Lampensteuerung.

Zeigt die Lampen des angemeldeten Benutzers an und formatiert geplante Einschalt- und Ausschaltzeiten.

### create_lamp(request)

Die Ansicht zum Hinzufügen einer neuen Lampe.

- **POST**: Nimmt das Formular für die Lampe entgegen, speichert sie und erstellt Statistiken für die Lampe.
- **GET**: Zeigt das Formular zum Hinzufügen einer Lampe an.

# API-Dokumentation

## Beispiel für die Verwendung der API

Hier ist ein Beispiel, wie Sie die API verwenden können, um Lampendaten von Ihrer Django-Anwendung abzurufen:

```python
import requests

url = 'https://codyiron.com/api/devices/'
headers = {'Authorization': 'Token 1ba7dlpturpal7413697f05853b785ed06accfbb'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Gib die JSON-Daten aus
    lamp_data = response.json()

    for lamp in lamp_data:
        print(lamp)
else:
    print(f"Fehler: {response.status_code}")

response.close()

```
## Erläuterungen zum Beispielcode

Hier sind einige Erläuterungen zum bereitgestellten Beispielcode:

- `url`: Die URL Ihrer API-Endpunkte.
- `token`: Ihr API-Token, das Sie für die Authentifizierung verwenden.
- `headers`: Die Header für die HTTP-Anfrage, einschließlich des Authentifizierungstokens.
- `requests.get(url, headers=headers)`: Sendet eine GET-Anfrage an die API mit den angegebenen Parametern.
- `response.status_code`: Überprüft den HTTP-Statuscode der Antwort.
- `response.json()`: Parst die Antwort als JSON, wenn der Statuscode 200 ist.
- `for lamp in lamp_data: print(lamp)`: Durchläuft und gibt die Lampendaten aus.
- `response.close()`: Schließt die Verbindung zur API.
