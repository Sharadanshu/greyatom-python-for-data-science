# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
#step1
census = np.concatenate((data,new_record),axis=0)
age = census[:,0]
#step2
max_age = int(max(age))
min_age = int(min(age))
age_mean = round(np.mean(age),2)
age_std = round(np.std(age),2)
#step3
race_0 = census[(census[:,2] == 0)]
race_1 = census[(census[:,2] == 1)]
race_2 = census[(census[:,2] == 2)]
race_3 = census[(census[:,2] == 3)]
race_4 = census[(census[:,2] == 4)]
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
race = np.array([len_0,len_1,len_2,len_3,len_4])
minority_race = np.where(race == int(min(race)))[0][0]
#step4
senior_citizens = census[(census[:,0] > 60)]
working_hours_sum = int((senior_citizens.sum(axis=0))[6])
senior_citizens_len = len(senior_citizens)
avg_working_hours = round((working_hours_sum/senior_citizens_len),2)
#step5
high = census[(census[:,1] > 10)]
low = census[(census[:,1] <= 10)]
avg_pay_high = round(((high.mean(axis=0))[7]),2)
avg_pay_low = round(((low.mean(axis=0))[7]),2)




