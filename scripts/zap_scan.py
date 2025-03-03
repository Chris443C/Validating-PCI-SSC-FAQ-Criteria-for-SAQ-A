import sys
from zapv2 import ZAPv2

def zap_scan(target):
    api_key = 'your_zap_api_key'
    zap = ZAPv2(apikey=api_key)

    print(f'Starting ZAP scan on {target}')
    zap.urlopen(target)
    zap.spider.scan(target)
    while int(zap.spider.status()) < 100:
        pass

    zap.ascan.scan(target)
    while int(zap.ascan.status()) < 100:
        pass

    report = zap.core.htmlreport()
    with open('reports/zap_report.html', 'w') as f:
        f.write(report)

    print('ZAP scan completed. Report saved to reports/zap_report.html')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python zap_scan.py <target_url>')
        sys.exit(1)
    target_url = sys.argv[1]
    zap_scan(target_url)
