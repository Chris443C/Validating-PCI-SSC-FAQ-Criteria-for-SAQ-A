import sys
from zapv2 import ZAPv2

def zap_scan(target_url):
    zap = ZAPv2()
    print(f'Scanning {target_url} with OWASP ZAP...')
    zap.urlopen(target_url)
    zap.spider.scan(target_url)
    while int(zap.spider.status()) < 100:
        pass
    zap.ascan.scan(target_url)
    while int(zap.ascan.status()) < 100:
        pass
    report = zap.core.htmlreport()
    return report

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python zap_scan.py <target_url>')
        sys.exit(1)
    target_url = sys.argv[1]
    report = zap_scan(target_url)
    with open('reports/zap_report.html', 'w') as f:
        f.write(report)
    print('OWASP ZAP scan completed. Report saved to reports/zap_report.html')
