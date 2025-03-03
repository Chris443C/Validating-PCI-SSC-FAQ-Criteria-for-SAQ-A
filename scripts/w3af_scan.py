import subprocess
import sys

def w3af_scan(target_url):
    print(f'Scanning {target_url} with w3af...')
    script_content = f"""
plugins
output console,text_file
output config text_file
set output_file reports/w3af_report.txt
set verbose True
back
target
set target {target_url}
back
start
"""
    with open('scripts/w3af_script.w3af', 'w') as script_file:
        script_file.write(script_content)
    result = subprocess.run(['w3af_console', '-s', 'scripts/w3af_script.w3af'], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python w3af_scan.py <target_url>')
        sys.exit(1)
    target_url = sys.argv[1]
    report = w3af_scan(target_url)
    print('w3af scan completed. Check reports/w3
::contentReference[oaicite:35]{index=35}
 
