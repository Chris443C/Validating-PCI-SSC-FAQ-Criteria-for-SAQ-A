import subprocess
import sys
import os

def run_bandit(target_directory, output_format='txt', output_file='bandit_report.txt'):
    """
    Runs Bandit against the target directory and saves the report.

    :param target_directory: Directory containing Python code to scan.
    :param output_format: Format of the output report ('txt', 'html', 'json', etc.).
    :param output_file: Name of the file to save the report.
    """
    print(f"Running Bandit scan on {target_directory}...")
    command = [
        'bandit',
        '-r', target_directory,
        '-f', output_format,
        '-o', output_file
    ]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"Bandit scan completed successfully. Report saved to {output_file}")
    else:
        print(f"Bandit scan encountered issues:\n{result.stderr}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python bandit_scan.py <target_directory>")
        sys.exit(1)

    target_dir = sys.argv[1]

    if not os.path.isdir(target_dir):
        print(f"Error: {target_dir} is not a valid directory.")
        sys.exit(1)

    # Ensure the reports directory exists
    reports_dir = 'reports'
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    # Define the output report path
    report_path = os.path.join(reports_dir, 'bandit_report.txt')

    # Run Bandit scan
    run_bandit(target_dir, output_file=report_path)
