import subprocess
import sys

def nikto_scan(target_url):
    print(f'Scanning {target_url} with Nikto...')
    result = subprocess.run(['nikto', '-h', target_url], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python nikto_scan.py <target_url>')
        sys.exit(1)
    target_url = sys.argv[1]
    report = nikto_scan(target_url)
    with open('reports/nikto_report.txt', 'w') as f:
        f.write(report)
    print('Nikto scan completed. Report saved to reports/nikto_report.txt')
