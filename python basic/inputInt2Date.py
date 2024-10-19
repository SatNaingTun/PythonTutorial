
monthInp=int(input('Enter month (1-12):'))
yearInp=int(input("Enter a year:"))



dateStr="{year}-{month}-{date}".format(year=yearInp,month=monthInp,date=1)
print(dateStr)
# currentDate=datetime.strptime(dateStr, '%Y-%m-%d').date()
# year, month, day = map(int, dateStr.split('-'))
     
# d=date(year=yearInt,month=monthInt,day=1)
# print("first day of month is"+weekdays[currentDate.weekday()])