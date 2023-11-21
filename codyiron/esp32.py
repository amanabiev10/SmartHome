import network
import time
import urequests
from machine import Pin, PWM

pin_badezimmer = [13, 12, 14]
pin_schlafzimmer = [5, 4, 2]
pin_wohnzimmer = [15, 0, 2]
pin_flur = [4, 16, 17]

# Replace with your Wi-Fi credentials
WIFI_SSID = 'Vire'
WIFI_PASSWORD = 'pipo0102030405'


# Function to connect to Wi-Fi
def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)

    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.active(True)
        wlan.connect(ssid, password)

        # Wait for the connection to be established
        while not wlan.isconnected():
            time.sleep(1)

    print("Connected to WiFi.")
    print("IP Address:", wlan.ifconfig()[0])


connect_to_wifi(WIFI_SSID, WIFI_PASSWORD)


def set_rgb_color(led_pin, color):
    # Extrahiere die RGB-Werte aus dem Hex-Code
    red = int(color[1:3], 16)
    green = int(color[3:5], 16)
    blue = int(color[5:7], 16)

    # Initialisiere die PWM-Pins für die RGB-LED
    red_led = PWM(Pin(led_pin[0]), freq=5000, duty=red)
    green_led = PWM(Pin(led_pin[1]), freq=5000, duty=green)
    blue_led = PWM(Pin(led_pin[2]), freq=5000, duty=blue)

    # Warte eine Weile und schalte dann die LED aus
    time.sleep(5)

    # Schalte die LED aus
    red_led.duty(0)
    green_led.duty(0)
    blue_led.duty(0)


def turn_on(led_pin):
    # Initialisiere den PWM-Pin für die LED
    led = PWM(Pin(led_pin), freq=5000, duty=1023)  # duty=1023 entspricht 100% Helligkeit


def turn_off(led_pin):
    # Initialisiere den PWM-Pin für die LED und setze die Helligkeit auf 0 (aus)
    led = PWM(Pin(led_pin), freq=5000, duty=0)


def set_brightness(led_pin, brightness):
    # Begrenze die Helligkeit auf den Bereich von 0 bis 1023
    brightness = max(0, min(brightness, 1023))

    # Initialisiere den PWM-Pin für die LED
    led = PWM(Pin(led_pin), freq=5000, duty=brightness)


while True:
    url = 'https://codyiron.com/api/devices/'

    headers = {'Authorization': 'Token 1ba7dc1a099ab1e13697f05853b785ed06accfbb'}
    response = urequests.get(url, headers=headers)

    if response.status_code == 200:
        # Gib die JSON-Daten aus
        lampen_liste = response.json()

        for lampe in lampen_liste:
            lampe_id = lampe['id']
            lampe_name = lampe['name']
            lampe_status = lampe['status']
            lampe_color = lampe['color']
            lampe_brightness = lampe['brightness']

            if lampe_id == 1:
                if lampe_status:
                    # Lampe einschalten
                    turn_on(pin_badezimmer[0])
                    # Setze die Helligkeit
                    set_brightness(pin_badezimmer[0], lampe_brightness)
                    # Setze die Farbe
                    set_rgb_color(pin_badezimmer, lampe_color)
                else:
                    # Lampe ausschalten
                    turn_off(pin_badezimmer[0])
                print(f"{lampe_name}: {lampe_status}, {lampe_brightness}, {lampe_color}")
            elif lampe_id == 3:
                if lampe_status:
                    # Lampe einschalten
                    turn_on(pin_schlafzimmer[0])
                    # Setze die Helligkeit
                    set_brightness(pin_schlafzimmer[0], lampe_brightness)
                    # Setze die Farbe
                    set_rgb_color(pin_schlafzimmer, lampe_color)
                else:
                    # Lampe ausschalten
                    turn_off(pin_schlafzimmer[0])
                print(f"{lampe_name}: {lampe_status}, {lampe_brightness}, {lampe_color}")
            elif lampe_id == 4:
                if lampe_status:
                    # Lampe einschalten
                    turn_on(pin_wohnzimmer[0])
                    # Setze die Helligkeit
                    set_brightness(pin_wohnzimmer[0], lampe_brightness)
                    # Setze die Farbe
                    set_rgb_color(pin_wohnzimmer, lampe_color)
                else:
                    # Lampe ausschalten
                    turn_off(pin_wohnzimmer[0])
                print(f"{lampe_name}: {lampe_status}, {lampe_brightness}, {lampe_color}")
            elif lampe_id == 5:
                if lampe_status:
                    # Lampe einschalten
                    turn_on(pin_flur[0])
                    # Setze die Helligkeit
                    set_brightness(pin_flur[0], lampe_brightness)
                    # Setze die Farbe
                    set_rgb_color(pin_flur, lampe_color)
                else:
                    # Lampe ausschalten
                    turn_off(pin_flur[0])
                print(f"{lampe_name}: {lampe_status}, {lampe_brightness}, {lampe_color}")

    else:
        print(f"Fehler: {response.status_code}")

    response.close()
