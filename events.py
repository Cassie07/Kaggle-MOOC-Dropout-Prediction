# -*- coding: utf-8 -*-
import numpy as np
import csv

id=1
cp=0
cv=0
ca=0
cw=0
cd=0
cn=0
cpa=0
event=[]
with open('/Users/kexinding/Desktop/CSE447/activity_log.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0]=='enrollment_id':
            continue
        elif row[0]==str(id):
            if row[2]=='problem':
                cp=cp+1
                continue
            elif row[2]=='video':
                cv=cv+1
                continue
            elif row[2]=='access':
                ca=ca+1
                continue
            elif row[2]=='wiki':
                cw=cw+1
                continue
            elif row[2]=='discussion':
                cd=cd+1
                continue
            elif row[2]=='navigate':
                cn=cn+1
                continue
            elif row[2]=='page_close':
                cpa=cpa+1
                continue
        else:
            event_this_time=[]
            id=id+1
            event_this_time.append(str(cp))
            event_this_time.append(str(cv))
            event_this_time.append(str(ca))
            event_this_time.append(str(cw))
            event_this_time.append(str(cd))
            event_this_time.append(str(cn))
            event_this_time.append(str(cpa))
            event.append(event_this_time)
            print(event)
            cp = 0
            cv = 0
            ca = 0
            cw = 0
            cd = 0
            cn = 0
            cpa = 0
            if row[2]=='problem':
                cp=cp+1
                continue
            elif row[2]=='video':
                cv=cv+1
                continue
            elif row[2]=='access':
                ca=ca+1
                continue
            elif row[2]=='wiki':
                cw=cw+1
                continue
            elif row[2]=='discussion':
                cd=cd+1
                continue
            elif row[2]=='navigate':
                cn=cn+1
                continue
            elif row[2]=='page_close':
                cpa=cpa+1
                continue
print(event)
with open("/Users/kexinding/Desktop/CSE447/total_clean.csv","w",newline='') as csvfile:
    writer = csv.writer(csvfile)
    #先写入columns_name
    #writer.writerow(["index","a_name","b_name"])
    #写入多行用writerows
    writer.writerows(event)
