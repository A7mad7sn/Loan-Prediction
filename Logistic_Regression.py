#impoting Libraries :-
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
def Logistic_algorirthm(loan_Df):
    print ('--------------------------------------------------------------------------')
    print ('Using Logistic Regression :-')
    print ('------------------------------')
    #Variables and Features :-
    x = loan_Df.iloc[:,1:12].values
    y = loan_Df["Loan_Status"].values
    
    #Data Splitting :-
    x_train, x_test, y_train, y_test = train_test_split(x, y)
    
    #Data Training :-
    loan_Model = LogisticRegression()
    loan_Model.fit(x_train, y_train)
    
    #Prediction for printing accuracy :-
    y_predict = loan_Model.predict(x_test)
    print('Logistic Regression accuracy for Loan Prediction = ', metrics.accuracy_score(y_predict,y_test))
    print('Y _ Real : ',y_test)
    print("Y _ Predicted : ",y_predict)
    print ('------------------------------------------------------------------------')
