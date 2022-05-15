'''
한국 주차 정산 프로그램 (Korea Parking Payment program)
1. 차량 번호 (Car number) (Old car num: XXㅁXXXX)(New car num: XXXㅁXXXX)(X: number, ㅁ: Korean letter)
2. 시간 (Time)

가짜 주차 데이터를 활용 (Going to use fake parking data)
'''
from ctypes import WinDLL
import random
from random import randint
from datetime import datetime, timedelta
from faker import Faker
import re

def randomCarData():
    carData = {}

    # 자동차 번호판 데이터 생성 (Producing random car number data) (korean letters allowed to use for car license plate)
    carLetterList = ['가', '나', '다', '라', '마', '거', '너', '더', '러', '머', '버', '서', '어', '저', '고', '노', '도', '로', '모', '보', '소', '오', '조', '구', '누', '두', '루', '무', '부', '수', '우', '주', '아', '바', '사', '자', '배', '하', '허', '호', '국', '합', '육', '해', '공', ]
    
    carNewOldSelector = randint(0, 9)   # 나오는 숫자가 3이하면 구형, 4이상이면 신형 (num<=3: old, num >= 4: new)(Considering that there are more new license plates)

    carNumFront = ""
    carNumBack = ""
    if carNewOldSelector <= 3:
        for num in range(6):
            value = str(randint(0, 9))
            if num <= 1:
                carNumFront += value
            else:
                carNumBack += value
        carNum = carNumFront + random.choice(carLetterList) + carNumBack
    else: 
        for num in range(7):
            value = str(randint(0, 9))
            if num <= 2:
                carNumFront += value
            else:
                carNumBack += value
        carNum = carNumFront + random.choice(carLetterList) + carNumBack
    carData['차량번호'] = carNum    # 차량번호 means 'car number'

    # 입차 시간 (일주일 이내 단기주차) (Enter time) (Only short parking period within a week)
    fake = Faker()
    currentTime = datetime.now()
    oneWeekBefore = currentTime - timedelta(weeks=1)
    randomDate = fake.date_time_between(start_date = oneWeekBefore, end_date = currentTime)
    enterTime = str(randomDate)
    carData['입차시간'] = enterTime    # 입차시간 means 'the time car entered to the parking lot'

    # 주차 시간 (Parking time)
    parkingTime = str(currentTime - randomDate)
    carData['주차시간'] = parkingTime   # 주차시간 means 'parking time'

    return carData

# 차량 데이터 10개 만들기 (Make 100 car data)
def sampleListCreator(sampleNum):
    carDatas = []
    while True:
        if sampleNum == 0:
            break
        else:
            carDatas.append(randomCarData())
            sampleNum -= 1
    return carDatas

def parkingPayment(carDatas):    
    print("30분 기본요금: 1,000원\n추가 10분 500원\n일일 요금 30,000원\n")   # Base rate for 30mins: 1,000krw, every 10mins: 500krw, max fare for day: 30,000krw
    carNumInput = input("차량번호 4자리를 입력하세요: ")    # Input last 4 digits of your car number
    matchCar = []
    for car in carDatas:
        if car['차량번호'][-4:] == carNumInput:
            matchCar.append(car)
        else:
            continue
    
    carIndex = 1
    for car in matchCar:
        print("{0}. {1}".format(carIndex, car['차량번호']))
        carIndex += 1

    myCarIndex = int(input("해당 차량의 번호를 골라주세요: ")) - 1  # "Please select your car" (With full car number). Since we are getting only last 4 digits of car, there might be more than one cars having same last digits. 
    print("\n")
    days = re.compile('\d(?=[ days])')
    parkingDays = re.findall(days, matchCar[myCarIndex]['주차시간'])
    if not parkingDays:
        parkingDays = 0
    else:
        parkingDays = int(parkingDays[0])
    
    hours = re.compile('(?<![:|\d])\d{1,2}(?=[:])')
    parkingHours = re.findall(hours, matchCar[myCarIndex]['주차시간'])
    
    minutes = re.compile('(?<=[:])\d{2}(?=[:])')
    parkingMinutes = re.findall(minutes, matchCar[myCarIndex]['주차시간'])

    totalMinutes = int(parkingHours[0])*60 + int(parkingMinutes[0])

    if parkingDays == 0 and totalMinutes < 30:
        cost = 1000
    elif parkingDays == 0:
        exceedingMinutes = (totalMinutes - 30)//10
        cost = int(1000 + exceedingMinutes*500)
    elif totalMinutes < 30:
        cost = int(parkingDays*30000 + 1000)
    else:        
        exceedingMinutes = (totalMinutes - 30)//10
        cost = int(parkingDays*30000 + exceedingMinutes*500 + 1000)
   
    print("차량번호: {0}\n입차시간: {1}\n주차시간: {2}\n요금: {3}원".format(matchCar[myCarIndex]['차량번호'], matchCar[myCarIndex]['입차시간'], matchCar[myCarIndex]['주차시간'], cost))
    
carDatas = sampleListCreator(10)
print(carDatas)
print("\n")
parkingPayment(carDatas)