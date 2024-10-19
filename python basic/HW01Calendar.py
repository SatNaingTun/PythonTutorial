from datetime import datetime,timedelta

# print(date_str)
# print(date_obj.weekday())

month30days={"September":9,"April":4,"June":6,"November":11}

weekdays = ["Mon", "Tue", "Wed","Thur", "Fri", "Sat", "Su"] 

def getNumbersOfDay():
    if(month==2):
        if(year%4==0):
            return 29
        else:
            return 28
    else:
        if month in list(month30days.values()):
            return 30
        else:
            return 31

def printCalendar():
    separater='\t'
    print(separater.join(weekdays))
    global currentDate,month
    max=getNumbersOfDay()
    wd=currentDate.weekday()
    # board = []
    for x in range(1,max+1):
        # print(currentDate)
        y=1
        for i in range(0,7):
            
            if(x==1 and i!=wd):
                print('',end='\t')
            # print("current day:"+str(x)+" Current week day: "+str(wd)+"week day:"+str(i))
            if(i==wd):
                print(x,end='\t')
                currentDate=currentDate+timedelta(days=1)
                wd=currentDate.weekday()
                if(i==6):
                    print("\n")
                break
            
                # print("blank "+str(y)+"\n")
                # y+=1
                
                           
 
if __name__=="__main__":
    year = int(input('Enter a year: '))
    month = int(input('Enter month (1-12):'))
    currentDate = datetime(year, month, 1)
    date_str = currentDate.strftime('%Y-%m-%d')
    printCalendar()