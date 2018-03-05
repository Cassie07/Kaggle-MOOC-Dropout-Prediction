from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import xgboost as xgb
from sklearn import tree
import numpy as np
import csv

username=[]
with open('/Users/kexinding/Desktop/CSE447/username.csv','r') as f:
    reader=csv.reader(f)
    for u in reader:
        username.append(u)
print(username)

day=[]
with open('/Users/kexinding/Desktop/CSE447/day.csv','r') as f:
    reader=csv.reader(f)
    for d in reader:
        day.append(d)
print(day)


y_train=[]
with open('/Users/kexinding/Desktop/CSE447/train_label.csv','r') as f:
    reader = csv.reader(f)
    for gt in reader:
        y_train.append(gt[1])
y_model=y_train[0:72325]
y_model=np.array(y_model)

x_train=[]
i=0
with open('/Users/kexinding/Desktop/CSE447/activity_update.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        row.append(username[i][0])
        row.append(day[i][0])
        x_train.append(row)
        i=i+1
x_model=x_train[0:72325]  # training data
x_model=np.array(x_model)
print(x_model)
x_predict=x_train[72325:120543] #predict data
#xp=np.array(x_predict)
x_predict=np.array(x_predict)
#print(x_predict)





predict_prob=[]
term=[]
num=72326
#for i in range(1,129):
#model = KNeighborsClassifier(n_neighbors=300)
#model = tree.DecisionTreeClassifier(criterion='gini')
#model= RandomForestClassifier()
#model= GradientBoostingClassifier(n_estimators=280, learning_rate=0, max_depth=2, random_state=0)
#param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'binary:logistic' }
#num_round = 2
param_dist = {'objective':'binary:logistic','rate_drop':'0.5','eta':'0.1','subsample':'0.8','colsample_bytree': '0.8',}
model = xgb.XGBClassifier(**param_dist)
# Or you can use: clf = xgb.XGBClassifier(**param_dist)
model.fit(x_model, y_model)
#model= xgb.train(param,x_model,num_round)
#model.fit(x_model, y_model)
#p predict
predict=model.predict_proba(x_predict)[:,1]
print(predict.shape)
predict=predict.tolist()
print(predict)
for j in range(48217):
    term.append(num)
    term.append(predict[j])
    predict_prob.append(term)
    print(predict_prob)
    term=[]
    num=num+1


with open("/Users/kexinding/Desktop/CSE447/result_dt.csv","w",newline='') as csvfile:
    writer = csv.writer(csvfile)
    #先写入columns_name
    #writer.writerow(["index","a_name","b_name"])
    #写入多行用writerows
    writer.writerows(predict_prob)

    #accuracy=model.score(np.array(x_test),np.array(y_test))
    #print('****************',accuracy)
    #accuracy1.append(1-accuracy)

#plt.plot(accuracy1)
#plt.show()


