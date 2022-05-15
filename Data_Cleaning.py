#importing Libraries
import pandas as pd 
def Data_Cleaning():
    #Data Loading 
    loan_Df = pd.read_csv("loan_data.csv")
    
    #Filling Empty cells at Column"Gender"(Once'Male' , Once'Feamle') :-
    G_check = 0
    for i in loan_Df.index:
        if loan_Df["Gender"][i] != 'Male' and loan_Df["Gender"][i] != 'Female':
            if G_check % 2 == 0:
                loan_Df["Gender"][i] = "Male"
                G_check = G_check + 1
            else :
                loan_Df["Gender"][i] = "Female"
                G_check = G_check + 1
                
    #Replacing Wrong Data at Column "Dependents" :-
    for i in loan_Df.index:
        if loan_Df.loc[i , "Dependents"] == "3+":
            loan_Df.loc[i , "Dependents"] =  3    
            
    #Filling Empty cells at Column"Dependents" with 0 :-
    loan_Df.fillna(0,inplace = True)
    
    #Filling Empty cells at Column"Self_Employed"(Once'Yes' , Once'No') :-
    SE_check = 0
    for i in loan_Df.index:
        if loan_Df["Self_Employed"][i] != 'Yes' and loan_Df["Self_Employed"][i] != 'No':
            if SE_check % 2 == 0:
                loan_Df["Self_Employed"][i] = "Yes"
                SE_check = SE_check + 1
            else :
                loan_Df["Self_Employed"][i] = "No"
                SE_check = SE_check + 1
                
    #Filling Empty cells at Column"LoanAmount" with mean value :-
    for i in loan_Df.index:
        if loan_Df["LoanAmount"][i] == 0:
            loan_Df["LoanAmount"][i] = loan_Df["LoanAmount"].mean()
    
    #Filling Empty cells at Column"Loan_Amount_Term" with mean value :-
    for i in loan_Df.index:
        if loan_Df["Loan_Amount_Term"][i] == 0:
            loan_Df["Loan_Amount_Term"][i] = loan_Df["Loan_Amount_Term"].mean()
            
    #Filling Empty cells at Column"Credit_History"(Once 1 , Once 0) :-
    CH_check = 0
    for i in loan_Df.index:
        if loan_Df["Credit_History"][i] != 1 and loan_Df["Gender"][i] != 0:
            if CH_check % 2 == 0:
                loan_Df["Credit_History"][i] = 1
                CH_check = CH_check + 1
            else :
                loan_Df["Credit_History"][i] = 0
                CH_check = CH_check + 1
    #Replacing String Values with Numeric Values at Columns("Gender","Married","Education","Self_Employed","Property_Area"):-
    loan_Df["Gender"].replace('Male',1,inplace = True)
    loan_Df["Gender"].replace('Female',0,inplace = True)
    loan_Df["Married"].replace('No',0,inplace = True)
    loan_Df["Married"].replace('Yes',1,inplace = True)
    loan_Df["Education"].replace('Not Graduate',0,inplace = True)
    loan_Df["Education"].replace('Graduate',1,inplace = True)
    loan_Df["Self_Employed"].replace('No',0,inplace = True)
    loan_Df["Self_Employed"].replace('Yes',1,inplace = True)
    loan_Df["Property_Area"].replace('Urban',0,inplace = True)
    loan_Df["Property_Area"].replace('Rural',1,inplace = True)
    loan_Df["Property_Area"].replace('Semiurban',2,inplace = True)
    return loan_Df          