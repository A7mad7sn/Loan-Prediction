# imporing Modules
import Data_Cleaning
import Logistic_Regression
import Decision_Tree
#Soon SVM Module will be imported !


#Data Cleaning & Preprocessing :-
loan_Df = Data_Cleaning.Data_Cleaning()

#Getting Features from User :-
print ('Enter Values : ' )
Gender = input('*Gender ? (Male/Female) : ')
if (Gender.lower() == 'male'):
    Gender = 1
elif(Gender.lower() == 'female'):
    Gender = 0
else:
    print('Invalid Gender it Will be "Male" by default !')
    Gender = 1
Married = input('*Married ? (Yes/No) : ')
if (Married.lower() == 'yes'):
    Married = 1
elif(Married.lower() == 'no'):
    Married = 0
else:
    print('Invalid Status it Will be "No" by default !')
    Gender = 1
Dependents = input('*Num of Dependents ? : ')
if Dependents.isnumeric() == False:
    print ('Please Enter Only Numeric Data !')
    Dependents = input('*Num of Dependents ? : ')
Education = input('*Education (Graduate/Not Graduate) ? : ')
if (Education.lower() == 'graduate'):
    Education = 1
elif(Education.lower() == 'not Graduate'):
    Education = 0
else:
    print('Invalid Education it Will be "Graduate" by default !')
    EducationGender = 1
Self_Employed = input('*Self_Employed ? (Yes/No) : ')
if (Self_Employed.lower() == 'yes'):
    Self_Employed = 1
elif(Self_Employed.lower() == 'no'):
    Self_Employed = 0
else:
    print('Invalid status it Will be "Yes" by default !')
    Self_Employed = 1
ApplicantIncome = input('*ApplicantIncome : ')
if ApplicantIncome.isnumeric() == False:
    print ('Please Enter Only Numeric Data !')
    ApplicantIncome = input('*ApplicantIncome : ')
CoapplicantIncome = input('*CoapplicantIncome : ')
if CoapplicantIncome.isnumeric() == False:
    print ('Please Enter Only Numeric Data !')
    CoapplicantIncome = input('*CoapplicantIncome : ')
LoanAmount = input('*LoanAmount : ')
if LoanAmount.isnumeric() == False:
    print ('Please Enter Only Numeric Data !')
    LoanAmount = input('*LoanAmount : ')
Loan_Amount_Term = input('*Loan_Amount_Term : ')
if Loan_Amount_Term.isnumeric() == False:
    print ('Please Enter Only Numeric Data !')
    Loan_Amount_Term = input('*Loan_Amount_Term : ')
Credit_History = input('*Credit_History (1/0) : ')
if Credit_History.isnumeric() == False:
    print ('Please Enter Only Numeric Data (1 Or 0) !')
    Credit_History = input('*Credit_History (1/0) : ')
Property_Area = input('*Property_Area ?(Urban/Rural/Semiurban) : ')
if (Property_Area.lower() == 'urban'):
    Property_Area = 0
elif(Property_Area.lower() == 'rural'):
    Property_Area = 1
elif(Property_Area.lower() == 'semiurban'):
    Property_Area = 2
else:
    print('it seems to be another Area , it will be Added')
    Property_Area = 3

#Collecting them into on Variable :-
features = [[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]]

#Using Different Models for Prediction :-
Logistic_Regression.Logistic_Preddiction(loan_Df,features)
Decision_Tree.Decision_Tree(loan_Df, features)
#soon SVM Will be Called !