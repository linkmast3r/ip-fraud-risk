import sys
import requests
import re
## variables globales
url = "https://scamalytics.com/ip/"

try:
    nombre_archivo = input("\nNombre del archivo de proxies >> ")
    handler = open(nombre_archivo)
except FileNotFoundError:
    print('Archivo {} no encontrado'.format(nombre_archivo))
    exit()


for line in handler:
    pieces = line.split(":")
    url_parsed = url + pieces[0]
    
    port = pieces[1]

    page = requests.get(url_parsed)
    html = page.text
 
    pattern_score = r'"score":(["])(?:(?=(\\?))\2.)*?\1'
    score = re.search(pattern_score, html).group()

    pattern_ip = r'"ip":(["])(?:(?=(\\?))\2.)*?\1,'
    ip = re.search(pattern_ip, html).group()
    
    ip_piece = ip.split('"')
    score_piece = score.split('"')

    proxy = ip_piece[3] + ":" + port
    score_parsed = int(score_piece[3])

    print("Proxy: " + proxy + "Riesgo de fraude: " + str(score_parsed))
   
    if score_parsed < 10:
        results = open("results.txt", "a")
        result = proxy
        results.write(result)

print('\n\n[*] Proxies con un score menor a 10 fueron guardadas a "results.txt"')   
