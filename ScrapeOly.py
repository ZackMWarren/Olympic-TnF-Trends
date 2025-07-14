import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

#event url is different for 2020 and 2024
#https://www.olympics.com/en/olympic-games/paris-2024/results/athletics/men-long-jump
#https://www.olympics.com/en/olympic-games/tokyo-2020/results/athletics/men-s-long-jump
#https://www.olympics.com/en/olympic-games/rio-2016/results/athletics/long-jump-men


#https://www.olympics.com/en/olympic-games/paris-2024/results/athletics/men-100m
#https://www.olympics.com/en/olympic-games/tokyo-2020/results/athletics/men-s-100m
#https://www.olympics.com/en/olympic-games/rio-2016/results/athletics/100m-men



def Scrape_Event(eventInp):
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    allResults = []

    years = range(1960, 2025, 4)
    olympicLocation = [
        "rome-1960",
        "tokyo-1964",
        "mexico-city-1968",
        "munich-1972",
        "montreal-1976",
        "moscow-1980",
        "los-angeles-1984",
        "seoul-1988",
        "barcelona-1992",
        "atlanta-1996",
        "sydney-2000",
        "athens-2004",
        "beijing-2008",
        "london-2012",
        "rio-2016",
        "tokyo-2020",
        "paris-2024"
    ]
    
    for num, year in enumerate(years):
        print(f"getting {olympicLocation[num]}...")
        event = eventInp
        event = event.replace(" ", "-")
        gender = "men"
        
        location = olympicLocation[num]
        if year == 2020:
            eventUrl = f"{gender}-s-{event}"
        if year == 2024:
            eventUrl = f"{gender}-{event}"
        else:
            eventUrl = f"{event}-{gender}"

        url = f"https://www.olympics.com/en/olympic-games/{location}/results/athletics/{eventUrl}"
        response = requests.get(url, headers = headers)
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find_all("span", attrs={"data-cy": "result-info-content"})
        
        for result in results:
            try:
                result = float(result.text.strip())
                allResults.append({"Year": year, "Results": result})
            except:
                continue
            
        time.sleep((random.randint(1,3)*0.1))
    return allResults
            

    
    


    
    
    
    
