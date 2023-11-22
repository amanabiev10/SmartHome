from machine import Pin, PWM
import network, time, urequests

# GPIO-Pins für die RGB-LED festlegen
lampe_pins = [
    [14, 12, 27, 26],  # Lampe 1
    [15, 13, 33, 32],  # Lampe 2
    [2, 14, 22, 21],  # Lampe 3
    [4, 23, 18, 5],  # Lampe 4
    [16, 17, 19, 15],  # Lampe 5
    [25, 26, 21, 19]  # Lampe 6
]

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


# GPIO initialisieren
def initialize_lamp_pins(common, red, green, blue):
    common_cathode = Pin(common, Pin.OUT)
    red_led = PWM(Pin(red), freq=1000, duty=0)
    green_led = PWM(Pin(green), freq=1000, duty=0)
    blue_led = PWM(Pin(blue), freq=1000, duty=0)

    return common_cathode, red_led, green_led, blue_led


# Funktion zur Einstellung der Farbe und Helligkeit
def set_color(red_led, green_led, blue_led, red, green, blue, brightness):
    # Helligkeit anpassen
    red = int(red * brightness / 100)
    green = int(green * brightness / 100)
    blue = int(blue * brightness / 100)

    # LEDs steuern (Duty Cycle für PWM)
    red_led.duty(int((255 - red) / 255 * 1023))
    green_led.duty(int((255 - green) / 255 * 1023))
    blue_led.duty(int((255 - blue) / 255 * 1023))


# Funktion zur Konvertierung von Hex-String zu RGB
def hex_to_rgb(hex_string):
    return (
        int(hex_string[1:3], 16),
        int(hex_string[3:5], 16),
        int(hex_string[5:], 16)
    )


# Funktion zum Ein- und Ausschalten der RGB-LED
def toggle_led(state):
    # Gemeinsame Kathode steuern
    common_cathode.value(state)


while True:
    url = 'https://codyiron.com/api/devices/'

    headers = {'Authorization': 'Token 1ba7dc1a099ab1e13697f05853b785ed06accfbb'}
    response = urequests.get(url, headers=headers)

    if response.status_code == 200:
        # Gib die JSON-Daten aus
        lampen_liste = response.json()

        for lampe in range(len(lampen_liste)):
            lampe_status = lampen_liste[lampe]['status']
            lampe_color = lampen_liste[lampe]['color']
            lampe_brightness = lampen_liste[lampe]['brightness']

            common_cathode, red_led, green_led, blue_led = initialize_lamp_pins(common=lampe_pins[lampe][0],
                                                                                red=lampe_pins[lampe][1],
                                                                                green=lampe_pins[lampe][2],
                                                                                blue=lampe_pins[lampe][3])
            color = hex_to_rgb(lampe_color)
            set_color(red_led, green_led, blue_led, *color, lampe_brightness)
            if lampe_status and lampe_brightness > 0:

                common_cathode.value(1)
            else:
                common_cathode.value(0)
    else:
        print(f"Fehler: {response.status_code}")
