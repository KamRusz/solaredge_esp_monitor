import urequests as requests
import time


for i in range(5):
    raw_data = requests.get(url='https://monitoringapi.solaredge.com/site/2897834/currentPowerFlow?api_key=666PT1BSVOMVFXEPESUFYWULCE1WPYPM').json()['siteCurrentPowerFlow']
    #from_grid = requests.get(url='https://monitoringapi.solaredge.com/site/2897834/currentPowerFlow?api_key=666PT1BSVOMVFXEPESUFYWULCE1WPYPM').json()['siteCurrentPowerFlow']['GRID']['currentPower']
    from_grid = raw_data['GRID']['currentPower']
    from_sun = raw_data['PV']['currentPower']
    total_consumption = raw_data['LOAD']['currentPower']
    #to_grid_total = requests.get(url='https://monitoringapi.solaredge.com/site/2897834/meters?meters=FeedIn&startTime=2022-09-24%2011:00:00&endTime=2022-09-25%2013:00:00&api_key=666PT1BSVOMVFXEPESUFYWULCE1WPYPM').json()['meterEnergyDetails']['meters'][0]['values'][0]['value']
    from_sun = requests.get(url='https://monitoringapi.solaredge.com/site/2897834/currentPowerFlow?api_key=666PT1BSVOMVFXEPESUFYWULCE1WPYPM').json()['siteCurrentPowerFlow']['PV']['currentPower']
    revenue = requests.get(url='https://monitoringapi.solaredge.com/site/2897834/overview?api_key=666PT1BSVOMVFXEPESUFYWULCE1WPYPM').json()['overview']['lifeTimeData']['revenue']
    
    #print("pobór z sieci:",r.json()['siteCurrentPowerFlow']['GRID']['currentPower'],"kW")
    #print("produkcja:",r.json()['siteCurrentPowerFlow']['PV']['currentPower'],"kW")
    #print("eksport:",x.json()['meterEnergyDetails']['meters'][0]['values'][0]['value']/1000000,"MWh")
    #revenue = z.json()['overview']['lifeTimeData']['revenue']
    #print("przychód",revenue,"zł")
    #print(f"% zwrotu:{(revenue/1900):.1f}%")
    print(from_grid, from_sun, total_consumption)
    #print(produkcjaipobor)
    time.sleep(1)
