#coding:utf8
import datetime
import numpy as np
import csv
import re

def time_differ(date1='12:55:05',date2='13:15:05'):
    '''
    @传入是时间格式如'12:55:05'
    '''
    date1=datetime.datetime.strptime(date1,"%H:%M:%S")
    date2=datetime.datetime.strptime(date2,"%H:%M:%S")
    if date1 < date2:
        return date2-date1
    else:
        return date1-date2


id=1
days=[]
second2=0
second1=0
timee=[]
times=[]
times_terminal=[]
collect=[]
count=0
num=0
with open('/Users/kexinding/Desktop/CSE447/activity_log.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0]=='enrollment_id':
            continue
        else:
            if row[0]==str(id):
                time = row[1]
                day = re.findall('(\d.+?)T', time)
                if day not in days:
                    if days==[]:
                        days.append(day)
                        num=num+1
                        second = re.findall('T(.*)', time)
                        collect.append(second)
                        count=count+1
                    else:
                        second1 = collect[0]
                        #print(second1)
                        str1 = ''
                        second1 = str1.join(second1)
                        second1 = second1
                        #print(count)
                        second2 = collect[count - 1]
                        #print(second2)
                        str2 = ''
                        second2 = str2.join(second2)
                        period = time_differ(second1, second2)
                        secondsDiff = round((period.total_seconds()) / 3600, 1)
                        period = str(secondsDiff)
                        timee.append(period)
                        count = 1
                        collect=[]
                        second = re.findall('T(.*)', time)
                        collect.append(second)
                        days.append(day)
                        num=num+1
                        #print(days)
                else:
                    second = re.findall('T(.*)', time)
                    collect.append(second)
                    count=count+1
            else:
                second1 = collect[0]
                #print(second1)
                str1 = ''
                second1 = str1.join(second1)
                second1 = second1
                # print(count)
                second2 = collect[count - 1]
                #print(second2)
                str2 = ''
                second2 = str2.join(second2)
                period = time_differ(second1, second2)
                secondsDiff = round((period.total_seconds()) / 3600, 1)
                period = str(secondsDiff)
                timee.append(period)
                #print(timee)
                total=0
                for n in range(num):
                    total=total+float(timee[n])
                #print(round(total,1))
                times_terminal.append(round(total,2))
                times.append(times_terminal)
                times_terminal=[]
                id=id+1
                count=0
                timee=[]
                collect=[]
                time=row[1]
                day = re.findall('(\d.+?)T', time)
                days=[]
                num=1
                days.append(day)
                second = re.findall('T(.*)', time)
                collect.append(second)
                count = count + 1
                print(times)