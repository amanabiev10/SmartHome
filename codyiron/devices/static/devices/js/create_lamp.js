// Ajax-Code hier hinzufügen
$("#lampForm").on("submit", function (event) {
    event.preventDefault();
    var formData = $(this).serialize();
    var url = $(this).attr("action");

    $.ajax({
        type: "POST",
        url: url,
        data: formData,
        success: function (data) {
            // Hier können Sie die Seite aktualisieren oder bestimmte Elemente aktualisieren
            console.log("Formular erfolgreich gesendet:", data);
        },
        error: function (error) {
            console.error("Fehler beim Senden des Formulars:", error);
        }
    });
});
