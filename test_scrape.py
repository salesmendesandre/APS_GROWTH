import urllib.request
import re

url = "https://produccioncientifica.usal.es/investigadores?buscar=Lozano+Murciego"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print("HTML length:", len(html))
        # Find links to /investigadores/\d+
        links = re.findall(r'href="(/investigadores/\d+/[^"]*)"', html)
        print("Profile links:", list(set(links)))
except Exception as e:
    print(e)
