#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      developer
#
# Created:     26/03/2018
# Copyright:   (c) developer 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import datetime
import calendar

error = 'input salah'
error1 = 'tidak bisa diproses'

def makeDate(dd,mm,yyyy):
    date = {'dd': dd, 'mm': mm, 'yyyy': yyyy}
    if isValidDate(date):
        date = datetime.date(yyyy, mm, dd)
        return date
    else:
        return False

def printDate(date):
    if isValidDate(date):
        date = date.strftime("%A,%d %B %Y")
        return date

def isValidDate(date):
    stat = False
    if isinstance(date, datetime.date): return True
    else:
        if date:
            for key in date:
                if isinstance(date[key], int) and date[key] > 0: status = True
                else: return False
            if status:
                if date['mm'] > 12:stat = False
                else:
                    month = calendar.monthrange(date['yyyy'],  date['mm'])
                    max_day = month[1]
                    if date['dd'] <= max_day: stat = True
    return stat

def nextDate(date):
    if isinstance(date, datetime.date):
        date = date + datetime.timedelta(1)
        return date
    else:
		print error1

def prevDate(date):
    if isinstance(date, datetime.date):
        date = date - datetime.timedelta(days=1)
        return date
    else:print error1

def nextNDate(date, n):
    if isinstance(date, datetime.date) and isinstance(n, int) and n > -1:
        date = date + datetime.timedelta(days=n)
        return date
    else:print error1

def prevNDate(date, n):
    if isinstance(date, datetime.date) and isinstance(n, int) and n > -1:
        date = date - datetime.timedelta(days=n)
        return date
    else:print error1

def isEq(date1, date2):
    return True if date1 == date2 else False

def isBefore(date1, date2):
    return True if date1 < date else False

def isAfter(date1, date2):
    if date1  > date2: return True
    else:return False


#date = makeDate('a',01, 2001)
#date1 = makeDate(25,1, 2011)
#print date
#print printDate(date)
#print isValidDate(date)
#print nextDate(date)
#print prevDate(date)
#print nextNDate(date, 10)
#print prevNDate(date, 365)
#print isEq(date, date1)
#print isBefore(date, date1)
#print isAfter(date, date1)
#print printDate(date)