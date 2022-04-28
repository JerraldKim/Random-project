def ToDoList():
    def showList(lst):
        index = 1
        for content in lst:
            print("{0}. {1}".format(index, content))
            index += 1
    toDoList = []
    numCount = 1
    selectLang = int(input("Language setting(언어 설정)(Input option number)(번호를 입력하세요): 1.English, 2.한국어\n"))

    if selectLang == 1:
        while True:
            operation = int(input("Which of the following options do you want to use?(Input option number) \n1.Add, 2.Modify, 3.Delete, 4.Exit\n"))
            if operation == 1:
                def thSelector(numCount):
                    if numCount == 1:
                        selector = 'st'
                    elif numCount == 2:
                        selector = 'nd'
                    elif numCount == 3:
                        selector = 'rd'
                    elif numCount >= 4:
                        selector = 'th'
                    return selector
                newToDoList = input("Input {0}{1} ToDoList: ".format(numCount, thSelector(numCount)))
                numCount += 1
                toDoList.append(newToDoList)
                showList(toDoList)
            elif operation == 2:
                modiNum = int(input("Input the index of list to modify: "))
                if modiNum > numCount:
                    print("Chosen index does not exist.")
                else:
                    indexNum = int(modiNum - 1)
                    replaceContent = input("Input content to be replaced: ")
                    toDoList[indexNum] = replaceContent
                    showList(toDoList)
            elif operation == 3:
                delNum = int(input("Input the index of list to delete: "))
                if delNum > numCount:
                    print("Chosen index does not exist.")
                else:
                    indexNum = int(delNum - 1)
                    del toDoList[indexNum]
                    numCount -= 1
                    showList(toDoList)
            elif operation == 4:
                print("End writing toDoList")
                showList(toDoList)
                break
            else:
                print("Wrong input. Please input a right number again.")

    elif selectLang == 2:
        while True:
            operation = int(input("다음 중 어떤 작업을 하시겠습니까?(번호를 입력하시오) \n1.추가, 2.수정, 3.삭제, 4.종료\n"))
            if operation == 1:
                newToDoList = input("{0}번째 ToDoList를 입력하시오: ".format(numCount))
                numCount += 1
                toDoList.append(newToDoList)
                showList(toDoList)
            elif operation == 2:
                modiNum = int(input("수정할 항목의 번호를 입력하시오: "))
                if modiNum > numCount:
                    print("선택하신 항목은 존재하지 않는 항목입니다.")
                else:
                    indexNum = int(modiNum - 1)
                    replaceContent = input("수정할 내용을 입력하시오: ")
                    toDoList[indexNum] = replaceContent
                    showList(toDoList)
            elif operation == 3:
                delNum = int(input("삭제할 항목의 번호를 입력하시오: "))
                if delNum > numCount:
                    print("선택하신 항목은 존재하지 않는 항목입니다.")
                else:
                    indexNum = int(delNum - 1)
                    del toDoList[indexNum]
                    numCount -= 1
                    showList(toDoList)
            elif operation == 4:
                print("toDoList 작성을 종료합니다")
                showList(toDoList)
                break
            else:
                print("잘못입력하셨습니다. 다시 입력바랍니다.")

    else:
        print("Wrong input. This program does not support other languages than English and Korean. Sorry.")
        print("잘못입력하셨습니다. 이 프로그램은 영어와 한국어를 제외하고 다른 언어를 지원하지 않습니다. 죄송합니다.")

ToDoList()
