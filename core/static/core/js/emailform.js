// Select the form element
const form = document.querySelector('#contactForm');
const submitButton = document.querySelector('#submitButton');

// Add submit event listener to the form
form.addEventListener('submit', async (event) => {
    // Prevent the default form submission
    event.preventDefault();

     // Display loading indicator (replace button text with three dots)
     submitButton.textContent = '...';

    // Get form data
    const formData = new FormData(form);

    try {
        // Fetch the /contact/ endpoint with POST method
        const response = await fetch('/contact/', {
            method: 'POST',
            body: formData
        });

        // Parse JSON response
        const data = await response.json();

        // Check if the request was successful
        if (response.ok) {
            // Show success message
            console.log("success")
            alert(data.message);
            // Optionally, clear form fields
            form.reset();
        } else {
            console.log("success")
            // Show error message
            alert(data.error);
        }
    } catch (error) {
        console.error('Error:', error);
        // Show error message
        alert('An error occurred while sending the message. Please try again later.');
    }finally {
        // Restore submit button text
        submitButton.textContent = 'Send';
    }
});
