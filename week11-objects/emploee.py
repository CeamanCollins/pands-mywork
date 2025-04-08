from timesheetentry import *

class Employee:
    timesheets = []

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def logminutes(self, project, minutes):
        timesheetentry = Timesheetentry(project, dt.datetime.now, minutes)
        self.timesheets.append(timesheetentry)

    def gettotaltime(self):
        total_minutes = 0
        for item in self.timesheets:
            total_minutes += item.duration
        return total_minutes

    def __str__(self):
        return self.first + ' ' + self.last
    
if __name__ == '__main__':
    test = Employee('Joe', 'Bloggs')
    test.logminutes('programming', 60)
    test.logminutes('checking',20)
    mins = test.gettotaltime()
    print(mins)