import subprocess
import sys

def nikto_scan(target):
    print(f'Starting Nikto scan on {target}')
    result = subprocess.run(['nikto', '-h', target], capture_output=True, text=True)
    with open('reports/nikto_report.txt', 'w') as f:
        f.write(result.stdout)
    print('Nikto scan completed. Report saved to reports/nikto_report.txt')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python nikto_scan.py <target_url>')
        sys.exit(1)
    target_url = sys.argv[1]
    nikto_scan(target_url)
