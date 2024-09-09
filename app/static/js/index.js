document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.upload-form');
    const modal = document.querySelector('.result-modal');
    const closeModalButton = document.querySelector('.modal-close-button');
    const instructionsContainer = document.querySelector('.instruction-results');
    const loader = document.querySelector('.loader');
    const loaderOverlay = document.querySelector('.loader-overlay')

    form.addEventListener('submit', function(event) {
        event.preventDefault(); 

        var formData = new FormData(form);

        loader.style.display = "block";
        loaderOverlay.style.display = "block";


        fetch('/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            instructionsContainer.textContent = data.instructions;
            loader.display.style = "none";
            loaderOverlay.display.style = "none";
            modal.style.display = 'flex';
        })
        .catch(error => {
            console.log(error.data)
            loader.display.style = "none";
            loaderOverlay.display.style = "none";
            alert('An error occurred while processing the request.');
        });
    });

    closeModalButton.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});