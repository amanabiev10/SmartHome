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

