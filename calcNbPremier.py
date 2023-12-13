
from curses.ascii import isdigit


def getPremierNum(start,end):
    premierNumList = []

    start = int(start)
    end = int(end)

    if start <= 1:
        start = 2
    
    # check range validite
    if end <= start:
        return []
    
    
    for num in range(start, end + 1):
        #special check for 2
        if num == 2:
            premierNumList.append(num)
            continue

        isPrem = True
        for div in range(2, num - 1):
            if num % div == 0:
                isPrem = False
                break

        if isPrem:
            premierNumList.append(num)
    
    return premierNumList

print("Please type two positive intergers for the begin and the end of the number range.")
while(True):
    startNum = input("The start of the range:")
    endNum = input("The end of the range:")

    #print(startNum.isdigit())
    #print(endNum.isdigit())
    if startNum.isdigit() and endNum.isdigit():
        break

    print("Please make sure to enter two positive intergers")

print(getPremierNum(startNum, endNum))
