document.getElementById('searchInput').addEventListener('input', function() {
    const query = this.value;

    if (query.length > 0) {
        fetch(`/citizen_search_ajax/?query=${query}`)
            .then(response => response.json())
            .then(data => {
                const resultsContainer = document.getElementById('resultsContainer');
                resultsContainer.innerHTML = '';  // Clear previous results

                if (data.length > 0) {
                    data.forEach(citizen => {
                        const row = document.createElement('div');
                        row.classList.add('result-row');
                        row.innerHTML = `
                            <div class="info">
                                <strong>Aadhaar: </strong>${citizen.aadhaar_number} |
                                <strong>Voter ID: </strong>${citizen.voter_id_number} |
                                <strong>Name: </strong>${citizen.citizen_name} |
                                <strong>Constituency: </strong>${citizen.constituency}
                            </div>
                            <button onclick="editCitizen(${citizen.id})">Edit</button>
                        `;
                        resultsContainer.appendChild(row);
                    });
                } else {
                    resultsContainer.innerHTML = '<p>No citizens found.</p>';
                }
            })
            .catch(error => {
                console.error('Error fetching search results:', error);
            });
    } else {
        document.getElementById('resultsContainer').innerHTML = '';  // Clear the container if search is empty
    }
});

function editCitizen(citizenId) {
    window.location.href = `/edit_citizen/${citizenId}/`;  // Redirect to the citizen's edit page
}
