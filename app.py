from flask import Flask, render_template, request, jsonify, send_file
from flask_socketio import SocketIO
import os
import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, async_mode='eventlet')

REPORTS_DIR = 'reports'
if not os.path.exists(REPORTS_DIR):
    os.makedirs(REPORTS_DIR)

def run_command(command):
    """Utility function to run a shell command."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout + result.stderr

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    # Run OWASP ZAP Scan
    zap_result = run_command(f'python3 scripts/zap_scan.py {url}')

    # Run Nikto Scan
    nikto_result = run_command(f'python3 scripts/nikto_scan.py {url}')

    # Run w3af Scan
    w3af_result = run_command(f'python3 scripts/w3af_scan.py {url}')

    # Combine results
    report_path = os.path.join(REPORTS_DIR, 'scan_report.txt')
    with open(report_path, 'w') as report_file:
        report_file.write('OWASP ZAP Scan Results:\n')
        report_file.write(zap_result)
        report_file.write('\n\nNikto Scan Results:\n')
        report_file.write(nikto_result)
        report_file.write('\n\nw3af Scan Results:\n')
        report_file.write(w3af_result)

    return jsonify({'message': 'Scan completed', 'report': report_path})

@app.route('/bandit_scan', methods=['POST'])
def bandit_scan():
    target_directory = request.form.get('target_directory')
    if not target_directory:
        return jsonify({'error': 'Target directory is required'}), 400

    # Ensure the target directory exists
    if not os.path.isdir(target_directory):
        return jsonify({'error': f'Target directory {target_directory} does not exist'}), 400

    # Define the output report path
    report_path = os.path.join(REPORTS_DIR, 'bandit_report.txt')

    # Run Bandit scan
    bandit_result = run_command(f'python3 scripts/bandit_scan.py {target_directory}')

    # Save the Bandit scan result to the report file
    with open(report_path, 'w') as report_file:
        report_file.write(bandit_result)

    return jsonify({'message': 'Bandit scan completed', 'report': report_path})

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join(REPORTS_DIR, filename), as_attachment=True)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
