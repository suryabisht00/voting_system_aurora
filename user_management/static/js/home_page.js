document.addEventListener('DOMContentLoaded', function() {
    // JavaScript code for animations and any interactivity can go here
});
if (window.history && window.history.pushState) {
    window.history.pushState(null, null, window.location.href);
    window.onpopstate = function() {
        window.history.pushState(null, null, window.location.href);
    };
}