// Funktion zum Umschalten des Lampenstatus
function toggleLamp(lampId) {
    var button = document.getElementById('licht' + lampId + '-button');
    var image = document.getElementById('image' + lampId);
    var status = button.textContent === 'Licht an' ? 'off' : 'on';

    fetch(`/api/toggle_lamp/${lampId}/?status=${status}`)
        .then(response => response.json())
        .then(data => {
            if (data.status === 'on') {
                button.textContent = 'Licht an';
                image.src = "/static/main/images/2910914.png";
            } else {
                button.textContent = 'Licht aus';
                image.src = "/static/main/images/2910890.png";
            }
        })
        .catch(error => {
            console.error('Fehler beim Umschalten der Lampe:', error);
        });
}

// Funktion zum Ändern der Helligkeit
function changeBrightness(lampId) {
    var slider = document.getElementById('brightness' + lampId + '-slider');
    var brightness = slider.value;

    fetch(`/api/change_brightness/${lampId}/?brightness=${brightness}`)
        .then(response => response.json())
        .then(data => {
            // Hier kannst du die Antwort vom Server verarbeiten
        })
        .catch(error => {
            console.error('Fehler beim Ändern der Helligkeit:', error);
        });
}

// Eventlistener für die Button-Klicks
document.getElementById('licht1-button').addEventListener('click', function () {
    toggleLamp(1);
});

// Eventlistener für die Helligkeitsslider
document.getElementById('brightness1-slider').addEventListener('input', function () {
    changeBrightness(1);
});
// Wiederholen Sie dies für andere Lampen