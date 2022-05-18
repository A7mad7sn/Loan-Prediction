#importing Libraries
import math
import pandas as pd 
import numpy as np
from sklearn.preprocessing import MaxAbsScaler
pd.set_option('display.max_rows', 900)
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 8000)
pd.set_option('display.max_colwidth', 8000)
def Data_Cleaning():
    
    #Data reading from the file :- 
    loan_Df = pd.read_csv("loan_data.csv")
    
    #Filling Empty cells at Column"Gender"(Once'Male' , Once'Feamle') :-
    G_check = 0
    for i in loan_Df.index:
        if loan_Df["Gender"][i] != 'Male' and loan_Df["Gender"][i] != 'Female':
            if G_check % 2 == 0:
                loan_Df["Gender"].replace(loan_Df["Gender"][i],'Male',inplace = True) 
                G_check = G_check + 1
            else :
                loan_Df["Gender"].replace(loan_Df["Gender"][i],'Female',inplace = True) 
                G_check = G_check + 1
                
    #Filling Empty cells at Column "Married" with 'No' :-
    loan_Df["Married"].fillna('No',inplace = True)
    
    #Replacing Wrong Data at Column "Dependents" :-
    loan_Df["Dependents"].replace('3+',3,inplace = True)
            
    #Filling Empty cells at Column"Dependents" with 0 :-
    loan_Df["Dependents"].fillna(0,inplace = True)
    
    #Filling Empty cells at Column"Self_Employed"(Once'Yes' , Once'No') :-
    SE_check = 0
    for i in loan_Df.index:
        if loan_Df["Self_Employed"][i] != 'Yes' and loan_Df["Self_Employed"][i] != 'No':
            if SE_check % 2 == 0:
                loan_Df["Self_Employed"].replace(loan_Df["Self_Employed"][i],'Yes',inplace = True) 
                SE_check = SE_check + 1
            else :
                loan_Df["Self_Employed"].replace(loan_Df["Self_Employed"][i],'Yes',inplace = True) 
                SE_check = SE_check + 1
                
    #Filling Empty cells at Column"LoanAmount" with mean value :-
    loan_Df["LoanAmount"].fillna(math.ceil(loan_Df["LoanAmount"].mean()),inplace = True)
    
    #Filling Empty cells at Column"Loan_Amount_Term" with mean value :-
    loan_Df["Loan_Amount_Term"].fillna(330,inplace = True)#330 is Average Term !
    
    #Filling Empty cells at Column"Credit_History"(Once 1 , Once 0) :-
    CH_check = 0
    for i in loan_Df.index:
        if loan_Df["Credit_History"][i] != 1 and loan_Df["Gender"][i] != 0:
            if CH_check % 2 == 0:
                loan_Df["Credit_History"].replace(loan_Df["Credit_History"][i],1,inplace = True) 
                CH_check = CH_check + 1
            else :
                loan_Df["Credit_History"].replace(loan_Df["Credit_History"][i],0,inplace = True) 
                CH_check = CH_check + 1
    
    #Replacing String Values with Numeric Values at Columns("Gender","Married","Education","Self_Employed","Property_Area"):-
    loan_Df["Gender"] = loan_Df["Gender"].map({'Male' : 1 , 'Female' : 0})
    loan_Df["Married"] = loan_Df["Married"].map({'Yes' : 1 , 'No' : 0})
    loan_Df["Education"] = loan_Df["Education"].map({'Graduate' : 1 , 'Not Graduate' : 0})
    loan_Df["Self_Employed"] = loan_Df["Self_Employed"].map({'Yes' : 1 , 'No' : 0})
    loan_Df["Property_Area"] = loan_Df["Property_Area"].map({'Urban' : 0 , 'Rural' : 1 , 'Semiurban' : 2})
    
    #Data Sclaing :-
    data_for_scale =  np.array(loan_Df.iloc[:,6:10])
    transformer = MaxAbsScaler()
    data_for_scale = transformer.fit_transform(data_for_scale)
    loan_Df.iloc[:,6:10] = data_for_scale
    return loan_Df          