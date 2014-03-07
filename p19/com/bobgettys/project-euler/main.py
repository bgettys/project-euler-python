'''
Created on Mar 6, 2014

@author: rgettys
'''

"""
    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# More interestingly, how many firsts of the month fell on a Sunday?

daysPerMonth = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
currentModulo = 2 # jan 1 1901 is a tuesday
firstOfMonthSundays = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        currentModulo += (29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28) if month == 2 else daysPerMonth[month-1]
        currentModulo %= 7
        if currentModulo == 0:
            firstOfMonthSundays += 1
print(firstOfMonthSundays)
            

if __name__ == '__main__':
    pass