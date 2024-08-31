from fastf1 import get_event_schedule
from datetime import datetime, timezone
race_info = {}

events = get_event_schedule(year=2024, include_testing=False)




print(events.columns)




def GetDateArray():
    session_dates = []

    for index, row in events.iterrows():
        
        session_dates.append(row['Session1DateUtc'])
        session_dates.append(row['Session2DateUtc'])
        session_dates.append(row['Session3DateUtc'])
        session_dates.append(row['Session4DateUtc'])        
        session_dates.append(row['Session5DateUtc'])
    formatted_dates = [datetime.strftime(date, "%Y-%m-%d") for date in session_dates]
    return formatted_dates
def CheckTodayPrix():
    now = datetime.now()


    utc_now = now.astimezone(timezone.utc)

    
    today = utc_now.date().strftime("%Y-%m-%d")
    
    date_array = GetDateArray()
    if today in date_array:
        x = GetRaceDictPrix()
        race = x[today]
        return race
    else:
        return None
    
def CheckTodayS1():
    now = datetime.now()


    utc_now = now.astimezone(timezone.utc)

    
    today = utc_now.date().strftime("%Y-%m-%d")
    
    date_array = GetDateArray()
    if today in date_array:
        x = GetRaceDictS1()
        race = x[today]
        return race
    else:
        return None
def CheckTodayS2():
    now = datetime.now()


    utc_now = now.astimezone(timezone.utc)

    
    today = utc_now.date().strftime("%Y-%m-%d")
    
    date_array = GetDateArray()
    if today in date_array:
        x = GetRaceDictS2()
        race = x[today]
        return race
    else:
        return None
def CheckTodayS3():
    now = datetime.now()


    utc_now = now.astimezone(timezone.utc)

    
    today = utc_now.date().strftime("%Y-%m-%d")
    
    date_array = GetDateArray()
    if today in date_array:
        x = GetRaceDictS3()
        race = x[today]
        return race
    else:
        return None
def CheckTodayS4():
    now = datetime.now()


    utc_now = now.astimezone(timezone.utc)

    
    today = utc_now.date().strftime("%Y-%m-%d")
    
    date_array = GetDateArray()
    if today in date_array:
        x = GetRaceDictS4()
        race = x[today]
        return race
    else:
        return None







def GetRaceDictPrix():
    
    for index, row in events.iterrows():
        race_name = row['EventName']
        race_type = row['EventFormat']
        race_date = row['Session5DateUtc'].strftime("%Y-%m-%d")  
        race_location = row["Country"]
        
        
        race_details = {"RaceName": race_name,'RaceType': race_type, 'RaceDate': race_date,"RaceLocation":race_location}
        
        
        race_info[race_date] = race_details
        
    return race_info
def GetRaceDictS1():
    
    for index, row in events.iterrows():
        race_name = row['EventName']
        race_type = row['EventFormat']
        race_date = row['Session1DateUtc'].strftime("%Y-%m-%d")  
        race_location = row["Country"]
        
        
        race_details = {"RaceName": race_name,'RaceType': race_type, 'RaceDate': race_date,"RaceLocation":race_location}
        
        
        race_info[race_date] = race_details
        
    return race_info
    

def GetRaceDictS2():
    
    for index, row in events.iterrows():
        race_name = row['EventName']
        race_type = row['EventFormat']
        race_date = row['Session2DateUtc'].strftime("%Y-%m-%d")  
        race_location = row["Country"]
        
        
        race_details = {"RaceName": race_name,'RaceType': race_type, 'RaceDate': race_date,"RaceLocation":race_location}
        
        
        race_info[race_date] = race_details
        
    return race_info
def GetRaceDictS3():
    
    for index, row in events.iterrows():
        race_name = row['EventName']
        race_type = row['EventFormat']
        race_date = row['Session3DateUtc'].strftime("%Y-%m-%d")  
        race_location = row["Country"]
        
        
        race_details = {"RaceName": race_name,'RaceType': race_type, 'RaceDate': race_date,"RaceLocation":race_location}
        
        
        race_info[race_date] = race_details
        
    return race_info
def GetRaceDictS4():
    
    for index, row in events.iterrows():
        race_name = row['EventName']
        race_type = row['EventFormat']
        race_date = row['Session4DateUtc'].strftime("%Y-%m-%d")  
        race_location = row["Country"]
        
        
        race_details = {"RaceName": race_name,'RaceType': race_type, 'RaceDate': race_date,"RaceLocation":race_location}
        
        
        race_info[race_date] = race_details
        
    return race_info
if __name__=="__main__":
    print("Hello World!")
    print(events)
    