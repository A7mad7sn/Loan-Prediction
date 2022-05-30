#impoting Libraries :-
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics

def svm_prediction(Data):
    print ('--------------------------------------------------------------------------')
    print ('Using SVM :-')
    print ('-------------')
   

    #Data Splitting :-
    x_train, x_test, y_train, y_test = Data

    #Data Training :-
    loan_model_svm = SVC(kernel = 'linear')
    loan_model_svm.fit(x_train,y_train)

    #Prediction for printing accuracy :-
    y_pred = loan_model_svm.predict(x_test)
    print('SVM accuracy for Loan Prediction = ',metrics.accuracy_score(y_pred,y_test))
    print("Prediction for Loan : ",y_pred)
    print ('--------------------------------------------------------------------------')

    