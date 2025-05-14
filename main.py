import requests
import datetime
import logger_custom as l


if __name__ == "__main__":
    response = requests.get("http://a.la-a.la/chart/chartdata.php?probe=11359212&type=lastdata")
    if response.status_code == 200: 
        data = response.json()
        date_time = datetime.datetime.fromtimestamp(data[1][0]).strftime('%Y-%m-%d %H:%M:%S')
        hodnoty = data[2]
    else: 
        l.logger.error("No values!")
        
    kluce = ["teplota_vzduchu", "prizemni_teplota", "teplota_pudy_10cm", \
                 "teplota_pudy_20cm", "teplota_pudy_30cm", "srazky", "vlhkost_vzduchu", \
                 "smer_vetru_stupne_180_jih", "oroseni_listu", "rychlost_vetru_mss", "vlhkost_pudy", \
                 "tlak_vzduchu", "globalni_zareni_Wm2", "napeti"]
    
    tabulka = dict(zip(kluce, hodnoty))
    
    '''
    #table = []
    #for key, value in tabulka.items():
    #    table.append(f"{key}: {value}")
    #table_str = "\n".join(table)
    
    #l.logger_all.info(f'{date_time} all: \n{table_str}')
    #l.logger_all.info(f'{date_time} all: {table}')
    '''
    l.logger.info(f"{date_time} temp: {tabulka['teplota_vzduchu']} wind: {tabulka['rychlost_vetru_mss']}")
    l.logger_all.info(f'{date_time} all: {tabulka}')