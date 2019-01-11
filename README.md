# openWeatherAlerts
A simple tool to see what the weather's going to do.

## Overview

Whenever our parking lots get icy, someone has to send an email warning everyone. It's monotonous and dumb. So here we are. 

## Setting it Up

First and foremost, you need an API key from OpenWeatherMap. It's free! 

https://openweathermap.org/api

Plug that into `config.py`, along with your zip code. 

Provide some values for the SMTP variables so you can actually receive email alerts. 

*NOTE:* This is intended to send an email to a distro list.

## How it Works

`weatherScraper.py` checks the weather for your zip code and adds the forecast to a list. The items in the `weathercodes.WeatherCodes.ICE` list are checked against the current forecast. If there's a match, icy conditions are assumed and an email is sent. If there isn't a match, the `weathercodes.WeatherCodes.RAIN` list is checked against the forecast and if there's a match, the `weathercodes.WeatherCodes.SNOW` list is checked. If there's a match in both `RAIN` _and_ `SNOW`, an email is sent regarding icy conditions. 

If there's an error when calling the API, an email is sent to the `ERROR_EMAIL` contact. The body of that email is the error message
