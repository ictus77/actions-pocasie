import requests
import datetime

URL = "http://a.la-a.la/chart/chartdata.php?probe=11359212&type=lastdata"
response = requests.get(URL)
data = response.json()
date_time_epoch = data[1]
date_time = datetime.datetime.fromtimestamp(date_time_epoch[0]).strftime('%Y-%m-%d %H:%M:%S')

print(date_time)

values = data[2]
teplota_vzduchu = values[0]
prizemni_teplota = values[1]
teplota_pudy_10cm = values[2]
teplota_pudy_20cm = values[3]
teplota_pudy_30cm = values[4]
srazky = values[5]
vlhkost_vzduchu = values[6]
smer_vetru_stupne_180_jih = values[7]
oroseni_listu = values[8]
rychlost_vetru_mss = values[9]
vlhkost_pudy = values[10]
tlak_vzduchu = values[11]
globalni_zareni_Wm2 = values[12]
napeti = values[13]

print(teplota_vzduchu)


# http://a.la-a.la/chart/chartdata.php?probe=11359212&type=lastdata
# [[1741953567], [1741957200], [4.4, 5.3, 6.7, 6.8, 6.5, 0.72, 100, 315, 0, 0.7, 29.2, 1002, 25.2, 13]]
# 2025-03-14 13:09:26
# 2025-03-14 14:10:00