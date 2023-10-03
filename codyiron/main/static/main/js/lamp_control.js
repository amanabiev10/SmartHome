$(document).ready(function () {
    // Verwende Delegierung, um auf Klicks zu reagieren
    $(document).on('click', '.on-off-button', function () {
        var lampId = $(this).data('lamp-id');
        var currentStatus = $(this).text().toLowerCase() === 'licht an';
        toggleLamp(lampId, currentStatus);
    });

    // AJAX-Aufruf, wenn sich der Helligkeitsschieberegler ändert
    $(document).on('input', '.brightness-slider', function () {
        var lampId = $(this).data('lamp-id');
        var brightness = $(this).val();
        updateBrightness(lampId, brightness);
    });

    // AJAX-Aufruf, wenn sich die Farbauswahl ändert
    $(document).on('input', '.color-picker', function () {
        var lampId = $(this).data('lamp-id');
        var color = $(this).val();
        updateColor(lampId, color);
    });

    function toggleLamp(lampId, currentStatus) {
        // Umkehrung des Status
        var newStatus = currentStatus ? 'False' : 'True';

        // AJAX-Aufruf
        $.ajax({
            url: '/toggle-lamp/' + lampId + '/',
            method: 'POST',
            data: {'status': newStatus},
            success: function (data) {
                // Aktualisiere den Button-Text
                var buttonText = newStatus === 'True' ? 'Licht an' : 'Licht aus';
                $('#licht' + lampId + '-button').text(buttonText);

                // Aktualisiere das Bild basierend auf dem neuen Status
                var imageUrl = newStatus === 'True' ? '/static/main/images/2910890.png' : '/static/main/images/2910914.png';
                $('#image' + lampId).attr('src', imageUrl);
            }
        });
    }

    function updateBrightness(lampId, brightness) {
        // AJAX-Aufruf
        $.ajax({
            url: '/update-brightness/' + lampId + '/',
            method: 'POST',
            data: {'brightness': brightness},
            success: function (data) {
                // Hier könntest du bei Bedarf weitere Aktualisierungen vornehmen
            }
        });
    }

    function updateColor(lampId, color) {
        // AJAX-Aufruf
        $.ajax({
            url: '/update-color/' + lampId + '/',
            method: 'POST',
            data: {'color': color},
            success: function (data) {
                // Hier könntest du bei Bedarf weitere Aktualisierungen vornehmen
            }
        });
    }
});
