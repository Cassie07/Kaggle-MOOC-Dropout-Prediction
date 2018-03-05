import numpy as np
import csv
import re


dict={}
user_name=[]
user_name_terminal=[]
num=0
with open('/Users/kexinding/Desktop/CSE447/enrollment_list.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0]=='enrollment_id':
            continue
        else:
            user=row[1]
            if user not in user_name:
                user_name.append(user)
                with open('/Users/kexinding/Desktop/CSE447/enrollment_list.csv', 'r') as f:
                    reader = csv.reader(f)
                    for rows in reader:
                        if rows[0] == 'enrollment_id':
                            continue
                        else:
                            if rows[1]==user:
                                num=num+1
                            else:
                                continue
                user_name.append(num)
                dict[user_name[0]]=user_name[1]
                num=0
                user_name=[]
            else:
                continue
        print(dict)
        print(row[0])

username=[]
usernames=[]
c=0
with open('/Users/kexinding/Downloads/enrollment_list.csv','r') as f:
    reader = csv.reader(f)
    for id in reader:
        if id[0]=='enrollment_id':
            continue
        else:
            username.append(id[0])
            id[1]=dict[id[1]]
            username.append(id[1])
            c=c+1
            usernames.append(username)
            username=[]
    print(c)

with open("/Users/kexinding/Desktop/CSE447/result_dt.csv","w",newline='') as csvfile:
    writer = csv.writer(csvfile)
    #先写入columns_name
    #writer.writerow(["index","a_name","b_name"])
    #写入多行用writerows
    writer.writerows(usernames)