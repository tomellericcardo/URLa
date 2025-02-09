// Log user position
function log_position() {
    navigator.geolocation.getCurrentPosition(function(position) {
        coordinates = position.coords.latitude + ',' + position.coords.longitude;
        var log_request = new XMLHttpRequest();
        log_request.open('GET', '/log/' + coordinates, true);
        log_request.send(null);
    });
}

// Periodically log position
document.addEventListener('DOMContentLoaded', function() {
    setInterval(log_position, 3000);
    log_position();
});
