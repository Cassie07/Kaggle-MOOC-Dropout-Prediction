# Kaggle-MOOC-Dropout-Prediction

A final project of cse447_data mining
leaderboard(rank): 23/68

description:
Students' high dropout rate on MOOC platforms (e.g., Coursera) has been heavily criticized, and predicting their likelihood of dropout would be useful for maintaining and encouraging students' learning activities. In this competition, you are challenged to build a predictor that can predict the chance that a student will drop out of an enrollment after observing his/her early course activities.

In particular, you have access to the student's course-relevant activities, such as working on course assignments, watching course videos, accessing the course wiki, etc.


File descriptions:

enrollment_list.csv - each line is a course enrollment record with an enrollment_id E, a user_id U and a course_id C, indicating that U has enrolled in C.
activity_log.csv - each line is a behavior record called "event". Each event contains the following information: enrollment_id, time, and event.
train_label.csv - each line is a dropout record of the enrollments in the training set. Each record contains two fields, enrollment_id E and dropout_prob, with dropout_prob = 1 indicating the student drops out of E.
sample_submission.csv - each line is a dropout record of the enrollments in the test set, which you are required to predict.

Data fields:
enrollment_id - an anonymous id unique to a given enrollment of a student
dropout_prob - the probability that the student drop out of the enrollment
time - the time when the event happens
We define 7 different event types:
problem - working on course assignments
video - watching course videos.
access - accessing other course objects except videos and assignments
wiki - accessing the course wiki
discussion - accessing the course forum
navigation - navigating to other part of the course.
page_close - closing the web page

