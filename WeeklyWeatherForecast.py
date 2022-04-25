import requests
import json
from datetime import datetime

apiKey = '8ef45cd0f548b32928a146dbd5e169a5'

cityCoordinateInfo = {'서울': [37.33, 126.58], '경기도': [37.58, 127.04], '강원도': [37.83, 128.22], '충청도': [36.30, 127.00], '전라도': [35.09, 126.51], '경상도': [36.15, 128.45], '부산': [35.17, 129.07], '대구': [35.52, 128.36], '대전': [36.21, 127.23], '제주도': [33.34, 126.10], '도쿄': [37.94, 138.75], '런던': [51.50, -0.12], '파리': [48.85, 2.34], '뉴욕': [40.70, 73.97]}
cityList = ['서울', '경기도', '강원도', '충청도', '전라도', '경상도', '부산', '대구', '대전', '제주도', '도쿄', '런던', '파리', '뉴욕']

print("검색 가능한 도시: {0}".format(cityList))
city = input("도시를 입력해주세요: ")
print("\n")

lat = str(cityCoordinateInfo[city][0])
lon = str(cityCoordinateInfo[city][1])

weatherUrl = 'https://api.openweathermap.org/data/2.5/onecall?lat=' + lat + '&lon=' + lon + '&exclude=current,minutely,hourly,alerts&appid=' + apiKey

response = requests.get(weatherUrl)

weatherData = response.json()

kelvin = 273.15

def Temp(tempData):
    timeTempList = []
    timeTempList.append(round((tempData['day'] - kelvin), 2))
    timeTempList.append(round((tempData['night'] - kelvin), 2))
    timeTempList.append(round((tempData['min'] - kelvin), 2))
    timeTempList.append(round((tempData['max'] - kelvin), 2))
    return timeTempList

def feelTemp(tempData):
    feelTempList = []
    feelTempList.append(round((tempData['day'] - kelvin), 2))
    feelTempList.append(round((tempData['night'] - kelvin), 2))
    return feelTempList

def compInfo(weatherData, dayNum): 
    dayTemp = Temp(weatherData['daily'][dayNum]['temp'])[0]
    nightTemp = Temp(weatherData['daily'][dayNum]['temp'])[1]
    minTemp = Temp(weatherData['daily'][dayNum]['temp'])[2]
    maxTemp = Temp(weatherData['daily'][dayNum]['temp'])[3]
    dayFeelTemp = feelTemp(weatherData['daily'][dayNum]['feels_like'])[0]
    nightFeelTemp = feelTemp(weatherData['daily'][dayNum]['feels_like'])[1]
    pressure = weatherData['daily'][dayNum]['pressure']
    humidity = weatherData['daily'][dayNum]['humidity']
    windSpeed = weatherData['daily'][dayNum]['wind_speed']
    cloudy = weatherData['daily'][dayNum]['clouds']
    print("낮기온: {0}도 / 밤기온: {1}도 / 최저기온: {2}도 / 최고기온: {3}도".format(dayTemp, nightTemp, minTemp, maxTemp))
    print("체감온도: {0}도(낮) / {1}도(밤)".format(dayFeelTemp, nightFeelTemp))
    print("기압: {0} hPa".format(pressure))
    print("습도: {0}%".format(humidity))
    print("풍속: {0}".format(windSpeed))
    print("구름: {0}%".format(cloudy))

if city in cityList:
    for day in range(8):
        if day == 0:
            print("{0}의 오늘 날씨입니다\n".format(city))
            compInfo(weatherData, day)
            print("\n")
        elif day == 1:
            print("{0}의 내일 날씨입니다\n".format(city))
            compInfo(weatherData, day)
            print("\n")
        elif day == 2:
            print("{0}의 내일 모레 날씨입니다\n".format(city))
            compInfo(weatherData, day)
            print("\n")
        else:
            print("{0}의 {1}일 후 날씨입니다\n".format(city, day))
            compInfo(weatherData, day)
            print("\n")
else:
    print("검색하신 도시가 없습니다")