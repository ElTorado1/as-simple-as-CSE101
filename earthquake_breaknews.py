import json
from urllib.request import urlopen
from tabulate import tabulate


apiUrl = "http://hasanadiguzel.com.tr/api/sondepremler"
sehir = input("Hangi sehirde deprem aratacakasınız? ").upper()

tablo_verileri = []
result = urlopen(apiUrl).read().decode('utf-8')
getData = json.loads(result)

j = 0
for data in getData['data']:
    if sehir in data['yer']:
        satir = [
            data['yer'],
            data['tarih'],
            data['saat'],
            data['ml'],
            data['enlem_n'],
            data['boylam_e']
        ]
        tablo_verileri.append(satir)
        j += 1
    if j>7:
        break
if tablo_verileri:
    headers = ["Yer", "Tarih", "Saat", "Büyüklük", "Enlem", "Boylam"]
    print(tabulate(tablo_verileri,headers=headers, tablefmt="fancy_grid"))