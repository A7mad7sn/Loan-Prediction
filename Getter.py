def FeaturesGetter():
    #Getting Features from User :-
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    print('                                                                        Enter your Values to Predict : ' )
    
    ID = input('--> Loan ID : ')
    
    Gender = input('--> Gender (Male/Female) : ')
    if (Gender.lower() == 'male'):
        Gender = 1
    elif(Gender.lower() == 'female'):
        Gender = 0
    else:
        print('Invalid Gender it Will be "Male" by default !')
        Gender = 1
    
    Married = input('--> Married (Yes/No) : ')
    if (Married.lower() == 'yes'):
        Married = 1
    elif(Married.lower() == 'no'):
        Married = 0
    else:
        print('Invalid Status it Will be "No" by default !')
        Married = 0
   
    while(True):
        Dependents = input('--> Num of Dependents  : ')
        if Dependents.isnumeric() == False:
            print ('Please Enter Only Numeric Data !')
            continue
        else:
            break
   
    Education = input('--> Education (Graduate/Not Graduate) : ')
    if (Education.lower() == 'graduate'):
        Education = 0
    elif(Education.lower() == 'not graduate'):
        Education = 1
    else:
        print('Invalid Education it Will be "Graduate" by default !')
        Education = 0
    
    Self_Employed = input('--> Self_Employed (Yes/No) : ')
    if (Self_Employed.lower() == 'yes'):
        Self_Employed = 1
    elif(Self_Employed.lower() == 'no'):
        Self_Employed = 0
    else:
        print('Invalid status it Will be "Yes" by default !')
        Self_Employed = 1
   
    while(True):
        ApplicantIncome = input('--> ApplicantIncome : ')
        if ApplicantIncome.isnumeric() == False:
            print ('Please Enter Only Numeric Data !')
            continue
        else:
            break
        
    while(True):
        CoapplicantIncome = input('--> CoapplicantIncome : ')
        if CoapplicantIncome.isnumeric() == False:
            print ('Please Enter Only Numeric Data !')
            continue
        else:
            break
        
    while(True):
        LoanAmount = input('--> LoanAmount : ')
        if LoanAmount.isnumeric() == False:
            print ('Please Enter Only Numeric Data !')
            continue   
        else:
            break
    
    while(True):    
        Loan_Amount_Term = input('--> Loan_Amount_Term : ')
        if Loan_Amount_Term.isnumeric() == False:
            print ('Please Enter Only Numeric Data !')
            continue
        else:
            break
     
    while(True):    
        Credit_History = input('--> Credit_History (1/0) : ')
        if Credit_History.isnumeric() == False:
            print ('Please Enter Only Numeric Data (1 Or 0) !')
            continue
        else:
            break
        
    Property_Area = input('--> Property_Area (Urban/Rural/Semiurban) : ')
    if (Property_Area.lower() == 'urban'):
        Property_Area = 2
    elif(Property_Area.lower() == 'rural'):
        Property_Area = 0
    elif(Property_Area.lower() == 'semiurban'):
        Property_Area = 1
    else:
        print('Invalid Property , it will be "Urban" by default')
        Property_Area = 2

    #Collecting them into on Variable :-
    features = [[Married,Dependents,Education,Self_Employed,CoapplicantIncome,Credit_History,Property_Area]]#only features selected by 'SelectPercentile'
    
    return features