document.addEventListener('DOMContentLoaded', function() {
    const scanForm = document.getElementById('scan-form');
    const banditScanForm = document.getElementById('bandit-scan-form');
    const resultDiv = document.getElementById('result');

    // Function to handle form submission
    function handleFormSubmit(form, endpoint) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            resultDiv.innerHTML = 'Processing... Please wait.';

            const formData = new FormData(form);
            fetch(endpoint, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    resultDiv.innerHTML = `<span style="color: red;">Error: ${data.error}</span>`;
                } else {
                    resultDiv.innerHTML = `
                        <p>Operation completed. <a href="/download/${data.report}">Download Report</a></p>
                        <pre>${data.output || ''}</pre>
                    `;
                }
            })
            .catch(error => {
                resultDiv.innerHTML = `<span style="color: red;">An error occurred: ${error.message}</span>`;
            });
        });
    }

    // Attach event listeners to both forms
    handleFormSubmit(scanForm, '/scan');
    handleFormSubmit(banditScanForm, '/bandit_scan');
});
