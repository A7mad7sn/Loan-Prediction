#impoting Libraries :-
from sklearn.linear_model import LogisticRegression
from sklearn import metrics


def Logistic_algorirthm(Data):
    print ('Using Logistic Regression :-')
    print ('------------------------------')
    
    #Data Splitting :-
    x_train, x_test, y_train, y_test = Data
    
    #Data Training :-
    loan_Model = LogisticRegression(solver='saga',penalty='l2')
    loan_Model.fit(x_train, y_train)
    
    #Prediction for printing accuracy :-
    y_predict = loan_Model.predict(x_test)
    print('Logistic Regression accuracy for Loan Prediction = ', metrics.accuracy_score(y_predict,y_test))
    print('Y _ Real : ',y_test)
    print("Y _ Predicted : ",y_predict)


def Logistic_Predictor(Data,features):
    print ('Using Logistic Regression :-')
    print ('------------------------------')
    
    #Data Splitting :-
    x_train, x_test, y_train, y_test = Data
    
    #Data Training :-
    loan_Model = LogisticRegression(solver='saga',penalty='l2')
    loan_Model.fit(x_train, y_train)
    #Prediction for features :-
    predicted_val = loan_Model.predict(features)
    print("Prediction for loan : ",predicted_val)
