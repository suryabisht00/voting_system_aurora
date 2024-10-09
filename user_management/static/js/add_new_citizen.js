// add_new_citizen.js

document.getElementById('citizenForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent default form submission
    let confirmed = confirm('Are you sure you want to add this citizen?');
    if (confirmed) {
        this.submit();  // If confirmed, submit the form
    }
});
