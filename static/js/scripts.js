document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('scan-form');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        resultDiv.innerHTML = 'Scanning... Please wait.';

        const formData = new FormData(form);
        fetch('/scan', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                resultDiv.innerHTML = `<span style="color: red;">Error: ${data.error}</span>`;
            } else {
                resultDiv.innerHTML = `
                    <p>Scan completed. <a href="/download/${data.report}">Download Report</a></p>
                    <pre>${data.output}</pre>
                `;
            }
        })
        .catch(error => {
            resultDiv.innerHTML = `<span style="color: red;">An error occurred: ${error.message}</span>`;
        });
    });
});
