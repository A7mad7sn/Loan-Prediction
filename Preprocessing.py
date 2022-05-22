#importing Libraries
import math
import pandas as pd 
import numpy as np
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.max_rows', 900)
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 8000)
pd.set_option('display.max_colwidth', 8000)

def Preprocessing():
    
    #Data reading from the file :- 
    loan_Df = pd.read_csv("loan_data.csv")
    
    #Filling Empty cells at Column"Gender"(Once'Male' , Once'Feamle') :-
    G_check = 0
    for i in loan_Df.index:
        if loan_Df.loc[i,"Gender"] != 'Male' and loan_Df.loc[i,"Gender"] != 'Female':
            if G_check % 2 == 0:
                loan_Df.loc[i,"Gender"] = 'Male'
                G_check = G_check + 1
            else :
                loan_Df.loc[i,"Gender"] = 'Female'
                G_check = G_check + 1
                
    #Filling Empty cells at Column "Married" with 'No' :-
    loan_Df["Married"].fillna('No',inplace = True)
    
    #Replacing Wrong Data at Column "Dependents" :-
    for i in loan_Df.index:
        if loan_Df.loc[i,"Dependents"] == '3+':
            loan_Df.loc[i,"Dependents"] = 3
      
    #Filling Empty cells at Column"Dependents" with 0 :-
    loan_Df["Dependents"].fillna(0,inplace = True)
    
    #Filling Empty cells at Column"Self_Employed"(Once'Yes' , Once'No') :-
    SE_check = 0
    for i in loan_Df.index:
        if loan_Df.loc[i,"Self_Employed"] != 'Yes' and loan_Df.loc[i,"Self_Employed"] != 'No':
            if SE_check % 2 == 0:
                loan_Df.loc[i, "Self_Employed"] = 'Yes'
                SE_check = SE_check + 1
            else :
                loan_Df.loc[i,"Self_Employed"] = 'No'
                SE_check = SE_check + 1
                
    #Filling Empty cells at Column"LoanAmount" with mean value :-
    loan_Df["LoanAmount"].fillna(math.ceil(loan_Df["LoanAmount"].mean()),inplace = True)
    
    #Filling Empty cells at Column"Loan_Amount_Term" with mean value :-
    loan_Df["Loan_Amount_Term"].fillna(330,inplace = True)#330 is Average Term !
    
    #Filling Empty cells at Column"Credit_History"(Once 1 , Once 0) :-
    CH_check = 0
    for i in loan_Df.index:
        if loan_Df.loc[i,"Credit_History"] != 1 and loan_Df.loc[i,"Credit_History"] != 0:
            if CH_check % 2 == 0:
                loan_Df.loc[i,"Credit_History"] = 1
                CH_check = CH_check + 1
            else :
                loan_Df.loc[i,"Credit_History"] = 0
                CH_check = CH_check + 1
    
    #Encoding ("Gender","Married","Education","Self_Employed","Property_Area"):-
    X = loan_Df.iloc[:,1:12]
    cols = ['Gender','Married','Education','Self_Employed','Property_Area']
    for c in cols:
        lbl = LabelEncoder()
        X[c] = lbl.fit_transform(list(X[c].values))
    loan_Df.iloc[:,1:12] = X  
    
    #Data Sclaing :-
    data_for_scale =  np.array(loan_Df.iloc[:,6:10])
    Scaler = MaxAbsScaler()
    data_for_scale = Scaler.fit_transform(data_for_scale)
    loan_Df.iloc[:,6:10] = data_for_scale
    
    
    return loan_Df          