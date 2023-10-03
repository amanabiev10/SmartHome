import requests

url = 'http://127.0.0.1:8000/api/devices'


headers = {'Authorization': 'Token db0b3ffb6f3a481062979f1f8b66809dbbc51373'}

# Sende eine GET-Anfrage
response = requests.get(url, headers=headers)

# Überprüfe, ob die Anfrage erfolgreich war (Statuscode 200)
if response.status_code == 200:
    # Gib die JSON-Daten aus
    lamp_data = response.json()

    for i in lamp_data:
        print(i)
else:
    print(f"Fehler: {response.status_code}")