import requests
import datetime

import logger_custom as l


if __name__ == "__main__":
    response = requests.get("http://a.la-a.la/chart/chartdata.php?probe=11359212&type=lastdata")
    if response.status_code == 200: 
        data = response.json()
        date_time = datetime.datetime.fromtimestamp(data[1][0]).strftime('%Y-%m-%d %H:%M:%S')
        teplota_vzduchu = data[2][0]
        prizemni_teplota = data[2][1]
        teplota_pudy_10cm = data[2][2]
        teplota_pudy_20cm = data[2][3]
        teplota_pudy_30cm = data[2][4]
        srazky = data[2][5]
        vlhkost_vzduchu = data[2][6]
        smer_vetru_stupne_180_jih = data[2][7]
        oroseni_listu = data[2][8]
        rychlost_vetru_mss = data[2][9]
        vlhkost_pudy = data[2][10]
        tlak_vzduchu = data[2][11]
        globalni_zareni_Wm2 = data[2][12]
        napeti = data[2][13]
    
        l.logger.info(date_time)
        l.logger.info(f'{date_time} temp: {teplota_vzduchu} wind: {rychlost_vetru_mss}')
        l.logger_all.info(f'{date_time} temp: {teplota_vzduchu} wind: {rychlost_vetru_mss} proste bordel')