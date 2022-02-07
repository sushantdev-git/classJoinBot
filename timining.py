from datetime import  datetime

classNames = [
                "Artificial Intelligence",  #0
                "Computer Network",  #1
                "Computer Network Lab", #2
                "Design and Analysis of Algorithms",#3
                "Design and Analysis of Algorithms Lab",#4
                "Operating System" ,#5
                "Operating System Lab",#6
                "Computer Organization and Architecture",#7
                "Computer Organization and Architecture Lab",#8
            ]

#(start time, end time, className[i]) timing of every class.
mondayTiming = [['09:00', '09:55',1], ['09:55','10:50',0], ['10:50','12:40',4], ['15:25','16:20',7]]
tuesdayTiming = [['09:00', '09:55',1], ['09:55', '11:45',4], ['15:25','16:20',3]]
wednesdayTiming = [['09:00', '09:55',5], ['09:55','10:50',0], ['12:40', '14:30',2], ['15:25','16:20',3]]
thrusdayTiming = [['09:00', '09:55', 1], ['09:55','10:50',7], ['11:45','13:35',2], ['15:25','16:20',5]]
fridayTiming = [['09:00', '09:55',5], ['09:55','10:50',7], ['13:35','14:30',8], ['14:30','16:20',6]]

def timediffSec(A, B):
    timeA = datetime.strptime(A, "%H:%M")
    timeB = datetime.strptime(B, "%H:%M")

    timediff = timeB-timeA
    return timediff.seconds

def addEndTime(timining):
    final = []
    n = len(timining)
    for i in range(n):
        final.append([timining[i][0], timediffSec(timining[i][0], timining[i][1]), classNames[timining[i][2]]])
    return final
        

def getDayTimining(day):
    if(day == "MON"): return addEndTime(mondayTiming)
    elif(day == "TUE"): return addEndTime(tuesdayTiming)
    elif(day == "WED"): return addEndTime(wednesdayTiming)
    elif(day == "THU"): return addEndTime(thrusdayTiming)
    elif(day == "FRI"): return addEndTime(fridayTiming)
    else: return []

print(getDayTimining("MON"))