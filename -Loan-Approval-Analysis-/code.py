# --------------
import pandas as pd
bank = pd.read_csv(path)
print(bank)
bank.shape
categorical_var = bank.select_dtypes(include = 'object')
numerical_var = bank.select_dtypes(include='number')




# --------------
# code starts here
import numpy as np
banks = bank.drop(columns=['Loan_ID' ])
#print(banks)
print(banks.isnull().sum())
bank_mode= banks.mode().iloc[0]

banks.fillna(bank_mode , inplace=True)
#print(banks.isnull().sum())
#print(banks.isnull().sum())
#fill_mode = lambda col: col.fillna(col.mode())
#banks.apply(fill_mode, axis=0)
#print(banks.head())
print(banks.isnull().sum())



#code ends here


# --------------
# Code starts here

avg_loan_amount = pd.pivot_table(banks , values='LoanAmount' , 
index=['Gender', 'Married' , 'Self_Employed'] , aggfunc={'LoanAmount': np.mean})

print(avg_loan_amount)
# code ends here



# --------------
# code starts here
loan_approved_se = len(banks[(banks['Self_Employed'] == 'Yes') & 
(banks['Loan_Status'] == 'Y')])

loan_approved_nse = len(banks[(banks['Self_Employed'] == 'No') & 
(banks['Loan_Status'] == 'Y')])

Loan_Status = 614
percentage_se = loan_approved_se / Loan_Status * 100
percentage_nse = loan_approved_nse / Loan_Status * 100
print (percentage_se)
print (percentage_nse)
# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x /12 )


big_loan_term = loan_term[loan_term >= 25].count()

print(big_loan_term)


# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby(['Loan_Status'])


loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History' ]]


mean_values = loan_groupby.agg([np.mean])

print(mean_values)
# code ends here


