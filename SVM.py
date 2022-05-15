#impoting Libraries :-
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics

def svm_prediction(loan_Df,features):
    print ('--------------------------------------------------------------------------')
    print ('Using SVM :-')
    print ('-------------')
    #Variables and Features :-
    x = loan_Df[["Gender","Married","Dependents","Education","Self_Employed","ApplicantIncome","CoapplicantIncome","LoanAmount","Loan_Amount_Term","Credit_History","Property_Area"]].values
    y = loan_Df["Loan_Status"].values

    #Data Splitting :-
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    #Data Training :-
    loan_model_svm = SVC()
    loan_model_svm.fit(x_train,y_train)

    #Prediction for printing accuracy :-
    y_pred = loan_model_svm.predict(x_test)
    print('SVM accuracy for Loan Prediction = ',metrics.accuracy_score(y_pred,y_test))
    y_pred = loan_model_svm.predict(features)
    print("Prediction for Loan : ",y_pred)
    print ('--------------------------------------------------------------------------')

    