import requests
import json
from datetime import datetime

apiKey = '8ef45cd0f548b32928a146dbd5e169a5'

selectLang = int(input("Language setting(언어 설정)(Input option number)(번호를 입력하세요): 1.English, 2.한국어\n"))

cityCoordinateInfoEng = {'Seoul': [37.33, 126.58], 'Gyeonggi-do': [37.58, 127.04], 'Gangwon-do': [37.83, 128.22], 'Chungcheong-do': [36.30, 127.00], 'Jeolla-do': [35.09, 126.51], 'Gyeongsang-do': [36.15, 128.45], 'Busan': [35.17, 129.07], 'Daegu': [35.52, 128.36], 'Daejeon': [36.21, 127.23], 'Jeju island': [33.34, 126.10], 'Tokyo': [37.94, 138.75], 'London': [51.50, -0.12], 'Paris': [48.85, 2.34], 'NewYork': [40.70, 73.97]}
cityListEng = ['Seoul', 'Gyeonggi-do', 'Gangwon-do', 'Chungcheong-do', 'Jeolla-do', 'Gyeongsang-do', 'Busan', 'Daegu', 'Daejeon', 'Jeju island', 'Tokyo', 'London', 'Paris', 'NewYork']

cityCoordinateInfoKor = {'서울': [37.33, 126.58], '경기도': [37.58, 127.04], '강원도': [37.83, 128.22], '충청도': [36.30, 127.00], '전라도': [35.09, 126.51], '경상도': [36.15, 128.45], '부산': [35.17, 129.07], '대구': [35.52, 128.36], '대전': [36.21, 127.23], '제주도': [33.34, 126.10], '도쿄': [37.94, 138.75], '런던': [51.50, -0.12], '파리': [48.85, 2.34], '뉴욕': [40.70, 73.97]}
cityListKor = ['서울', '경기도', '강원도', '충청도', '전라도', '경상도', '부산', '대구', '대전', '제주도', '도쿄', '런던', '파리', '뉴욕']

if selectLang == 1:
    print("City list: {0}".format(cityListEng))
    city = input("Input city: ")
    print("\n")
    lat = str(cityCoordinateInfoEng[city][0])
    lon = str(cityCoordinateInfoEng[city][1]) 
    weatherUrl = 'https://api.openweathermap.org/data/2.5/onecall?lat=' + lat + '&lon=' + lon + '&exclude=current,minutely,hourly,alerts&appid=' + apiKey

elif selectLang == 2:
    print("검색 가능한 도시: {0}".format(cityListKor))
    city = input("도시를 입력해주세요: ")
    print("\n")
    lat = str(cityCoordinateInfoKor[city][0])
    lon = str(cityCoordinateInfoKor[city][1])
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

def compInfo(weatherData, dayNum, selectLang): 
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
    if selectLang == 1:
        print("day temp: {0} celsius / night temp: {1} celsius / lowest temp: {2} celsius / highest temp: {3} celsius".format(dayTemp, nightTemp, minTemp, maxTemp))
        print("fell temp: {0} celsius(day) / {1} celsius(night)".format(dayFeelTemp, nightFeelTemp))
        print("pressure: {0} hPa".format(pressure))
        print("humidity: {0}%".format(humidity))
        print("wind speed: {0}".format(windSpeed))
        print("cloud: {0}%".format(cloudy))
    
    elif selectLang == 2:
        print("낮기온: {0}도 / 밤기온: {1}도 / 최저기온: {2}도 / 최고기온: {3}도".format(dayTemp, nightTemp, minTemp, maxTemp))
        print("체감온도: {0}도(낮) / {1}도(밤)".format(dayFeelTemp, nightFeelTemp))
        print("기압: {0} hPa".format(pressure))
        print("습도: {0}%".format(humidity))
        print("풍속: {0}".format(windSpeed))
        print("구름: {0}%".format(cloudy))

if selectLang == 1:
    if city in cityListEng:
        for day in range(8):
            if day == 0:
                print("Today's weather of {0}\n".format(city))
                compInfo(weatherData, day, 1)
                print("\n")
            elif day == 1:
                print("Tomorrow's weather of {0}\n".format(city))
                compInfo(weatherData, day, 1)
                print("\n")
            else:
                print("Weather of {0} after {1}days\n".format(city, day))
                compInfo(weatherData, day, 1)
                print("\n")
    else:
        print("City is not in the list")

elif selectLang == 2:
    if city in cityListKor:
        for day in range(8):
            if day == 0:
                print("{0}의 오늘 날씨입니다\n".format(city))
                compInfo(weatherData, day, 2)
                print("\n")
            elif day == 1:
                print("{0}의 내일 날씨입니다\n".format(city))
                compInfo(weatherData, day, 2)
                print("\n")
            elif day == 2:
                print("{0}의 내일 모레 날씨입니다\n".format(city))
                compInfo(weatherData, day, 2)
                print("\n")
            else:
                print("{0}의 {1}일 후 날씨입니다\n".format(city, day))
                compInfo(weatherData, day, 2)
                print("\n")
    else:
        print("검색하신 도시가 없습니다")
