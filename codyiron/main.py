import requests

url = 'https://codyiron.com/api/devices/'

headers = {'Authorization': 'Token 1ba7dc1a099ab1e13697f05853b785ed06accfbb'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Gib die JSON-Daten aus
    lampen_liste = response.json()

    for lampe in lampen_liste:
        print(lampe)

else:
    print(f"Fehler: {response.status_code}")

response.close()