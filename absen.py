#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      developer
#
# Created:     03/04/2018
# Copyright:   (c) developer 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def main():
    pass

if __name__ == '__main__':
    main()


import date_python, time_python

class absen():

    def __init__(self):
       pass

    def importText(self, file):
        file = open(file,  'r')
        results = []
        with file as inputfile:
            for line in inputfile:
                results.append(line.strip().split(','))
        return results

    def createRowData(self, file):
        text = self.importText(file)
        masuk = []
        i = 0
        for line in text:
            for string in line:
                string = string.replace(" ", "")
                nik = string[0:5]
                date = string[5:13]
                time = string[13:19]
                masuk.append({'nik':nik,  'masuk':{'date': date, 'time':time}})
        i += 1
        data = self.convDateTime(masuk)
        return data

    def convDateTime(self, data):
        retval = False
        for i in data:
             retval = True if i['nik'].isdigit() and len(i['nik']) == 5 else False
             i.update({'status':retval})
             if i['masuk']['date'][0:8].isdigit() and len(i['masuk']['date']) == 8:
                year = int(i['masuk']['date'][0:4])
                month = int(i['masuk']['date'][4:6])
                day = int(i['masuk']['date'][6:8])
                date = date_python.makeDate(day, month, year)
                if date:
                    i['masuk'].update({'date':date})
                else:
                    retval = False
                    i.update({'status':retval})
             else:
                retval = False
                i.update({'status':retval})
             if i['masuk']['time'][0:6].isdigit() and len(i['masuk']['time']) == 6:
                hour = int(i['masuk']['time'][0:2])
                minute = int(i['masuk']['time'][2:4])
                second = int(i['masuk']['time'][4:6])
                time = time_python.makeJam(hour, minute, second)
                if time:
                    i['masuk'].update({'time':time})
                    i.update({'keterangan':'Telat'}) if time_python.isJAfter(time, time_python.makeJam(7,0,0)) else i.update({'keterangan':''})
                else:
                    retval = False
                    i.update({'status':retval})
             else:
                retval = False
                i.update({'status':retval})
        return data

    def printData(self,data):
        for key in data:
            print 'Karyawan {nik} datang {date} {time} {keterangan}'.format(nik =  key['nik'], date = key['masuk']['date'], time = key['masuk']['time'], keterangan = key['keterangan'])


class absen2(absen): #gagalkan semua

    def printData(self, data):
        status = True
        for key in data:
            if key['status'] == False:status = False
        if not status:
            print
        else:
            absen.printData(self, data)

class absen3(absen): #gagalkan bawahnya

    def printData(self, data):
        for key in data:
            if key['status'] == False:
                del key
                break
            else:
                data = [key]
                absen.printData(self, data)

class absen4(absen):

    def printData(self, data):
        for key in data:
            if key['status'] == False:
                del key
            else:
                data = [key]
                absen.printData(self, data)


#absensi = absen()
absensi2 = absen2()
absensi3 = absen3()
absensi4 = absen4()

data2 = absensi2.createRowData('absen.txt')
data3 = absensi3.createRowData('absen.txt')
data4 = absensi4.createRowData('absen.txt')



#absensi.printData(data)
#print ('-----------------------------')
absensi2.printData(data2)
print ('-----------------------------')
absensi3.printData(data3)
print ('-----------------------------')
absensi4.printData(data4)
