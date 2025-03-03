document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('scan-form');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const url = document.getElementById('url').value;

        resultDiv.innerHTML = '<p>Scanning in progress...</p>';

        fetch('/scan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: url }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                resultDiv.innerHTML = `<p>Error: ${data.error}</p>`;
            } else {
                resultDiv.innerHTML = `
                    <p>Scan completed. <a href="/download/${data.report}" target="_blank">Download Report</a></p>
                    <pre>${data.output}</pre>
                `;
            }
        })
        .catch(error => {
            resultDiv.innerHTML = `<p>An error occurred: ${error.message}</p>`;
        });
    });
});
