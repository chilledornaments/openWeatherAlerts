class Config():
    ZIP_CODE = ""
    COUNTRY_CODE = "us"
    API_KEY = ""
    API_URL = "https://api.openweathermap.org/data/2.5/weather"
    API_PARAMETERS = {'zip': ZIP_CODE+","+COUNTRY_CODE, 'APPID': API_KEY}

    EMAIL_TO = 'distro@you.com'
    EMAIL_TO_NAME = 'Distro Name'
    EMAIL_FROM = 'noreply@you.com'
    EMAIL_FROM_NAME = ''
    MAIL_SERVER = ''

    ERROR_EMAIL = ''
    ERROR_EMAIL_TO_NAME = ''
    ERROR_EMAIL_SUBJECT = 'WeatherBot Error'
    

    ICY_EMAIL_SUBJECT = "Icy Parking Lot"


