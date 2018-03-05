import numpy as np
import csv
import re

times=[]
count=0
count_terminal=[]
counts=[]
id=1
with open('/Users/kexinding/Desktop/CSE447/activity_log.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0]=='enrollment_id':
            continue
        else:
            if row[0]==str(id):
                time=row[1]
                t = re.findall('(\d.+?)T', time)
                if t not in times:
                    times.append(t)
                    count=count+1
                else:
                    continue
            else:
                count_terminal.append(count)
                counts.append(count_terminal)
                print(counts)
                count_terminal=[]
                times=[]
                id=id+1
                time=row[1]
                t = re.findall('(\d.+?)T', time)
                times.append(t)
                count=1

with open("/Users/kexinding/Desktop/CSE447/result_dt.csv","w",newline='') as csvfile:
    writer = csv.writer(csvfile)
    #先写入columns_name
    #writer.writerow(["index","a_name","b_name"])
    #写入多行用writerows
    writer.writerows(counts)
