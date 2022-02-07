from datetime import datetime
import timeTable
import schedule
import time

e = datetime.now()

day = (e.strftime("%a"))
print(day)
print("program starts")


if day == "Mon":
    timeTable.monday()
elif day == "Tue":
    timeTable.tuesday()
elif day == "Wed":
    timeTable.wednesday()
elif day == "Thu":
    timeTable.thrusday()
elif day == "Fri":
    timeTable.friday()
else:
    print("no class")

while True: #this loop will run infinitely and check if any class is pending
    #event loop
    schedule.run_pending()
    print("running", datetime.now())
    time.sleep(60)#seconds
    
    if(len(schedule.jobs) == 0):
        print("No jobs pending")
        break


