# 打印日历 导入日历模块
import calendar
import time
year =int( input("Enter the year of the required calendar "))
month = int( input("Enter the month of the required calendar "))
print(calendar.month(year,month))  

print(time.asctime())