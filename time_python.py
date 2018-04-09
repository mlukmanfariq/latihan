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

error = 'input salah'
error1 = 'tidak bisa memproses, data tidak valid'


from datetime import date, datetime, time, timedelta

def makeJam(hh,mm,ss):
    jam = {'hh': hh, 'mm': mm, 'ss': ss}
    if isJValid(jam):
        jam  = time(hh,mm,ss)
        return jam
    else:
        return False

def printJam(jam):
   # jam = jam.strftime('%X')
    return jam

def isJValid(jam):
    stat = False
    if isinstance(jam, time): return True
    else:
        if jam:
            for key in jam:
                if isinstance(jam[key], int) and jam[key] >= 0: status = True
                else: return False
            if status:
                if jam['hh'] <= 23:
                    if jam['mm'] <= 59:
                        if jam['ss'] <= 59:stat = True
    return stat

def plusSecond(jam, n):
    if isinstance(n, int) and n > -1:
        t = datetime.combine(date.today(), jam) + timedelta(seconds=n)
        jam = t.time()
        return jam
    else:
		return error1

def minusSecond(jam, n):
    if isinstance(n, int) and n > -1:
        t = datetime.combine(date.today(), jam) - timedelta(seconds=n)
        jam = t.time()
        return jam
    else:return error1

def jamToSecond(jam):
    if isJValid(jam):
        tot_detik = jam.hour * 3600
        tot_detik = tot_detik + jam.minute * 60
        tot_detik = tot_detik + jam.second

        return tot_detik
    else:
		return error1

def isJBefore(jam1, jam2):
    return True if isJValid(jam1) and isJValid(jam2) and jam < jam2 else False


def isJAfter(jam1, jam2):
    return True if isJValid(jam1) and isJValid(jam2) and jam1 > jam2 else False

#jam = makeJam(1,1,1)
#jam1 = makeJam(4,2,1)
#print jam
#print isJValid(jam)
#print plusSecond(jam, 60)
#print minusSecond(jam, 3600)
#print jamToSecond(jam)
#print isJBefore(jam,jam1)
#print isJAfter(jam, jam1)
#print printJam(jam)

