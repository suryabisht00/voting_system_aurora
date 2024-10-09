document.addEventListener('DOMContentLoaded', function () {
    const searchBar = document.getElementById('searchBar');
    const candidateList = document.getElementById('candidateList');
    const editCandidateForm = document.getElementById('editCandidateForm');
    const editForm = document.getElementById('editForm');

    // Search candidates in real-time
    searchBar.addEventListener('input', function () {
        const query = searchBar.value.toLowerCase();
        const candidates = candidateList.getElementsByClassName('candidate-item');
        
        for (let candidate of candidates) {
            const name = candidate.querySelector('p').innerText.toLowerCase();
            const constituency = candidate.querySelector('p:nth-child(3)').innerText.toLowerCase();
            
            if (name.includes(query) || constituency.includes(query)) {
                candidate.style.display = '';
            } else {
                candidate.style.display = 'none';
            }
        }
    });

    // Open the edit form when edit button is clicked
    document.querySelectorAll('.editBtn').forEach(button => {
        button.addEventListener('click', function () {
            const candidateId = this.getAttribute('data-id');
            const candidateItem = document.querySelector(`.candidate-item[data-id="${candidateId}"]`);
            const name = candidateItem.querySelector('p').innerText;
            const constituency = candidateItem.querySelector('p:nth-child(3)').innerText;
            const party = candidateItem.querySelector('p:nth-child(4)').innerText;

            // Populate the edit form with existing data
            editCandidateForm.style.display = 'block';
            document.getElementById('edit_candidate_id').value = candidateId;
            document.getElementById('edit_candidate_name').value = name;
            document.getElementById('edit_constituency').value = constituency;
            document.getElementById('edit_party').value = party;
        });
    });
});
