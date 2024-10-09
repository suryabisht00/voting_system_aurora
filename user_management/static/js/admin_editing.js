// admin_editing.js

document.getElementById('addNewUserButton').addEventListener('click', function() {
    window.location.href = "{% url 'add_new_user' %}";
});

document.getElementById('editExistingUserButton').addEventListener('click', function() {
    window.location.href = "{% url 'edit_existing_user' %}";
});

document.getElementById('addEditCandidateButton').addEventListener('click', function() {
    window.location.href = "{% url 'add_edit_candidate' %}";
});
