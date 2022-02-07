import schedule
from join import *
import timining

def monday():
    for startTime,endTime in timining.getDayTimining("MON"):
        schedule.every().monday.at(startTime).do(joinClass,endTime)
    
def tuesday():
    for startTime,endTime in timining.getDayTimining("TUE"):
        schedule.every().tuesday.at(startTime).do(joinClass,endTime)

def wednesday():
    for startTime,endTime in timining.getDayTimining("WED"):
        schedule.every().wednesday.at(startTime).do(joinClass,endTime)

def thrusday():
    for startTime,endTime in timining.getDayTimining("THU"):
        schedule.every().thursday.at(startTime).do(joinClass,endTime)

def friday():
    for startTime,endTime in timining.getDayTimining("FRI"):
        schedule.every().friday.at(startTime).do(joinClass,endTime)

def dummy():
    schedule.every().friday.at("20:41").do(joinClass)


# Code for Timetable.py ends here 