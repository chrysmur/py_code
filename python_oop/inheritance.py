#!/usr/bin/python3
'''
Calendar  and Clock advance using multiple inheritance
Clock has _hour which we can access in the calendar clock class to advance calendar
'''


class Clock:
    '''Initialize and advance time using tick method'''

    def __init__(self, hour, minutes, seconds):
        self.set_clock(hour, minutes, seconds)

    def set_clock(self, hour, minutes, seconds):
        if type(hour) == int and 0 <= hour and hour < 24:
            self._hour = hour
        else:
            raise TypeError("Hour must be integers 0-23")
        if type(minutes) == int and 0 <= minutes and minutes < 60:
            self.__minutes = minutes
        else:
            raise TypeError("Minutes must be integers 0-59")
        if type(seconds) == int and 0 <= seconds and seconds < 60:
            self.__seconds = seconds
        else:
            raise TypeError("Seconds must be int 0-59")

    # return the value of time in a format
    @property
    def time(self):
        return "{0:02d} : {1:02d} : {2:02d}".format(self._hour, self.__minutes, self.__seconds)

    def tick(self):
        if self.__seconds == 59:
            if self.__minutes == 59:
                if self._hour == 23:
                    self._hour = 0
                else:
                    self._hour += 1
                self.__minutes = 0
            else:
                self.__minutes += 1
            self.__seconds = 0
        else:
            self.__seconds += 1


class Calendar:
    '''
    Class to define the calendar properties
    '''
    months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    style = "British"

    @staticmethod
    def leapyear(year):
        if (not year % 400) or ((not year % 4) and (year % 100)):
            return True
        else:
            return False

    def __init__(self, d, m, y):
        self.set_calendar(d, m, y)

    @property
    def date(self):
        return "{0:02d}-{1:02d}-{2:04d}".format(self.__d, self.__m, self.__y)

    def set_calendar(self, d, m, y):
        # check if its a leap year
        leap = self.leapyear(y)
        # validate months
        if m > 12 or m <= 0:
            raise ValueError("Invalid Month")
        # get max days of this month
        max_days = self.months[m-1]
        # make february 29 days for leap year
        if leap and m == 2:
            max_days += 1

        if (type(d) != int) or (d < 0 or d > max_days):
            raise ValueError(f"Invalid day for month {m}")
        else:
            self.__d = d

        if (type(m) != int) or (m <= 0 or m > 12):
            raise ValueError("Invalid month")
        else:
            self.__m = m

        if (type(d) != int) or (y < 0 or y > datetime.now().year):
            raise ValueError("Invalid Year, Future years not allowed")
        else:
            self.__y = y

    def advance(self):
        max_days = self.months[self.__m - 1]
        leap = self.leapyear(self.__y)
        if leap and self.__m == 2:
            max_days += 1

        if self.__d == max_days:
            self.__d = 1
            if self.__m == 12:
                self.__y += 1
                self.__m = 1
            else:
                self.__m += 1

        else:
            self.__d += 1


class CalendarClock(Calendar, Clock):

    def __init__(self, day, month, year, hour, minute, second):
        Calendar.__init__(self, day, month, year)
        Clock.__init__(self, hour, minute, second)

    def tick(self):
        hour_before = self._hour
        Clock.tick(self)
        hour_after = self._hour

        if hour_after < hour_before:
            Calendar.advance(self)

    def __str__(self):
        return self.date + ", " + self.time
