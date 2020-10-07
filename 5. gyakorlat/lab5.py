
class Clock:

    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.__hour = hours
        self.__minute = minutes
        self.__second = seconds

    def set(self, hours, minutes, seconds):
        self.__hour = hours
        self.__minute = minutes
        self.__second = seconds

    def get(self):
        return (self.__hour, self.__minute, self.__second)

    def tick(self):
        if self.__second == 59:
            self.__second = 0
            if self.__minute == 59:
                self.__minute = 0
                if self.__hour == 23:
                    self.__hour = 0
                else:
                    self.__hour += 1
            else:
                self.__minute += 1
        else:
            self.__second += 1

    def display(self):
        print("%2d:%2d:%2d" % (self.__hour, self.__minute, self.__second))

    def __str__(self):
        return "{}:{}:{}".format(self.__hour,self.__minute, self.__second)

c1 = Clock(2,25,16)
print(c1._hour)
c1.display()
for i in range(100):
    c1.tick()
print(c1)

class Calendar:

    months = [31,28,31,30,31,30,31,31,30,31,30,31]

    def __init__(self, day = 1, month = 1, year = 1900):
        self.__day = day
        self.__month = month
        self.__year = year

    def set(self, year, month, day):
        self.__day = day
        self.__month = month
        self.__year = year

    def get(self):
        return (self.__year, self.__month, self.__day)

    def __str__(self):
        return "A jelenlegi datum: {}.{}.{}.".format(self.__year, self.__month, self.__day)

    def leapyear(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False

    def advance(self):
        days_of_month = self.months[self.__month - 1]
        if self.leapyear(self.__year) and self.__month == 2:
            days_of_month += 1
        if self.__day == days_of_month:
            self.__day = 1
            if self.__month == 12:
                self.__month = 1
                self.__year += 1
            else:
                self.__month += 1
        else:
            self.__day += 1

class CalendarClock(Clock, Calendar):

    def __init__(self,year, month, day, hour = 0, minutes = 0, seconds = 0):
        Calendar.__init__(self,day, month, year)
        Clock.__init__(self, hour, minutes, seconds)

    def __str__(self):
        return Calendar.__str__(self) + " " + Clock.__str__(self)


cal1 = Calendar(2,3,1964)
# print(cal1)
# cal1.set(2020,10,6)
# print(cal1)
# for i in range(1000):
#     cal1.advance()
# print(cal1)

cc1 = CalendarClock(2020,10,6)
for i in range(1000):
    cc1.tick()
print(cc1.__str__())





