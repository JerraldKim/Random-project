def ToDoList():
    def showList(lst):
        index = 1
        for content in lst:
            print("{0}. {1}".format(index, content))
            index += 1
    toDoList = []
    numCount = 1
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

ToDoList()
