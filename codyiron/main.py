import requests

url = 'http://127.0.0.1:8000/api/devices'


headers = {'Authorization': 'Token 4fa2aa91acda47a155451ecd96cc670be888faba'}

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