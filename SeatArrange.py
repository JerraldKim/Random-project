import random

selectLang = int(input("Language setting(언어 설정)(Input option number)(번호를 입력하세요): 1.English, 2.한국어\n"))

def ordinalSuffixSelector(numCount):
    numEnd = numCount % 10
    if numEnd == 1:
        selector = 'st'
    elif numEnd == 2:
        selector = 'nd'
    elif numEnd == 3:
        selector = 'rd'
    elif numEnd >= 4:
        selector = 'th'
    elif numEnd == 0:
        selector = 'th'
    return selector

def nameInput(selectLang, deskNum):
    names = []
    personCount = 1
    if selectLang == 1:
        while True:
            peopleNum = len(names)
            if peopleNum == deskNum:
                print("Seats full. End adding new person.")
                break
            else:
                nameInput = input("Input {0}{1} person(enter 'Exit' to stop adding): ".format(personCount, ordinalSuffixSelector(personCount)))
                if nameInput == 'Exit':
                    break
                else:
                    names.append(nameInput)
                    personCount += 1
    
    elif selectLang == 2:
        while True:
            peopleNum = len(names)
            if peopleNum == deskNum:
                print("좌석이 꽉 찼습니다. 인원 추가를 종료합니다.")
                break
            else:
                nameInput = input("{0}번째 사람을 입력하세요(추가를 그만하고 싶으시면 '종료'를 입력해주세요): ".format(personCount))
                if nameInput == '종료':
                    break
                else:
                    names.append(nameInput)
                    personCount += 1
    return names

if selectLang == 1:
    widthDesk = int(input("Input numbers of desks in width: "))
    lengthDesk = int(input("Input numbers of desks in length: "))
    deskNum = widthDesk*lengthDesk
    nameList = nameInput(1, deskNum)
    peopleNum = len(nameList)
    emptySeats = int(deskNum - peopleNum)
    for i in range(emptySeats):
        nameList.append('empty')

elif selectLang == 2:
    widthDesk = int(input("가로 책상 수를 입력하세요: "))
    lengthDesk = int(input("세로 책상 수를 입력하세요: "))
    deskNum = widthDesk*lengthDesk
    nameList = nameInput(2, deskNum)
    peopleNum = len(nameList)
    emptySeats = int(deskNum - peopleNum)
    for i in range(emptySeats):
        nameList.append('공석')

def seatArrange():
    random.shuffle(nameList)
    widthCount = 1
    for name in nameList:
        print("{0}".format(name), end = '\t')
        if widthCount % widthDesk == 0:
            print("\n")
            widthCount += 1
        else:
            widthCount += 1

seatArrange()