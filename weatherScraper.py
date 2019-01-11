#!/usr/bin/env python3
import requests, json
from config import Config
from actions import ActionList
from weathercodes import WeatherCodes
from sys import exit

class WeatherScraper():
    
    def __init__(self):
        
        self.weatherScraper()

    def weatherScraper(self):
        self.r = requests.get(Config.API_URL, params=Config.API_PARAMETERS)
        
        if self.r.status_code == 200:
            self.JSON_RESPONSE = json.loads(self.r.text)
            self.WEATHER_FORECAST = self.JSON_RESPONSE['weather']
        
            self.weatherParser()
        else:
            self.error_()

    def weatherParser(self):

        WEATHER_DICT = []
        
        for weather in self.WEATHER_FORECAST:
            
            MAIN_DESCRIPTION = weather['description']
            WEATHER_DICT.append(MAIN_DESCRIPTION)

        # This list is auto icy, we can stop after checking against it if we find a match
        for ice_item in WeatherCodes.ICE:
            if ice_item in WEATHER_DICT:
                ActionList.ice_email(ActionList)
                exit(0)

        
        for rain_item in WeatherCodes.RAIN:
            # Check to see if there's rain
            if rain_item in WEATHER_DICT:
                # Check to see if there's also snow
                for snow_item in WeatherCodes.SNOW:
                    if snow_item in WEATHER_DICT:
                        ActionList.ice_email(ActionList)
                        exit(0)
                    exit(0)
            exit(0)

        
    def error_(self):
        ActionList.error_email(ActionList, str(self.r.text))

if __name__ == '__main__':
    WeatherScraper()




