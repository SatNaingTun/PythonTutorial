# import calendar

from datetime import datetime,timedelta

monthInp=int(input('Enter a year: '))
yearInp=int(input("Enter month number:"))

date_obj = datetime(yearInp, monthInp, 1)

month30days={"September":9,"April":4,"June":6,"November":11}

  
weekdays = ["Mon", "Tue", "Wed", 
        "Thur", "Fri", "Sat", "Su"] 

def getNumbersOfDay(monthDigit):
    if(monthDigit==2):
        if(yearInp%4==0):
            return 29
        else:
            return 28
    else:
        if monthDigit in list(month30days.values()):
            return 30
        else:
            return 31

def printCalendar():
    separater='\t'
    print(separater.join(weekdays))
    for x in range(1,30):
        print('\n') 
        for i in range(0,7):
            if(i==currentDate.weekday()):
                print(x,end='\t',flush=True)
                currentDate=currentDate+timedelta(days=1)
        
