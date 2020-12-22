# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)

#Code starts here
#step 1
categorical_var = bank_data.select_dtypes(include = 'object')
print(categorical_var.shape)
numerical_var = bank_data.select_dtypes(include = 'number')
print(numerical_var.shape)
#step 2
banks= bank_data.drop(columns='Loan_ID')
null_value = banks.isnull().sum()
print(null_value)
bank_mode = banks.mode().iloc[0]
banks.fillna(bank_mode, inplace=True)
print(banks.isnull().sum().values.sum())
print(banks.shape)
#step 3
avg_loan_amount = pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount',aggfunc='mean')
print(avg_loan_amount['LoanAmount'][1],2)
#step 4
loan_approved_se = (banks[(banks["Self_Employed"] == 'Yes') & (banks["Loan_Status"] == 'Y')])["Loan_Status"].count()
loan_approved_nse = (banks[(banks["Self_Employed"] == 'No') & (banks["Loan_Status"] == 'Y')])["Loan_Status"].count()
loan_Status = 614
percentage_se = round(((loan_approved_se/loan_Status)*100),2)
percentage_nse = round(((loan_approved_nse/loan_Status)*100),2)
print(percentage_se,percentage_nse)
#step 5
loan_term = banks['Loan_Amount_Term'].apply(lambda x : x/12)
big_loan_term = len(loan_term[loan_term>=25])
print(big_loan_term)
#step 6
loan_groupby = banks.groupby(['Loan_Status'])
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()
print(mean_values.iloc[1,0], 2)



