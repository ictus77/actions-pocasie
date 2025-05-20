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

#remove duplicate lines , as cron on github is running just random
### app log
with open("./app4.log", "r") as file_app: 
    lines_app = file_app.readlines()

unique_lines_app = list(dict.fromkeys(lines_app))

with open("./app4.log", "w") as file_app: 
    file_app.writelines(unique_lines_app)

### all log
with open("./all4.log", "r") as file_all: 
    lines_all = file_all.readlines()

unique_lines_all = list(dict.fromkeys(lines_all))

with open("./all4.log", "w") as file_all: 
    file_all.writelines(unique_lines_all)