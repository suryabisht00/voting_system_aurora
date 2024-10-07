function voteForCandidate(candidateId) {
    if (confirm("Are you sure you want to vote for this candidate?")) {
        // Hide all confirmation messages
        document.querySelectorAll('[id^="confirmation-"]').forEach(function(element) {
            element.style.display = 'none';
        });

        // Show the confirmation message for the selected candidate
        var selectedElement = document.getElementById('confirmation-' + candidateId);
        if (selectedElement) {
            selectedElement.style.display = 'block';
        } else {
            console.error('Confirmation element not found for candidateId:', candidateId);
        }
    }
}

document.addEventListener('DOMContentLoaded', function() {
    // JavaScript code to dynamically update images and text if needed
});