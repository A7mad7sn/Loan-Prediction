#impoting Libraries :-
from sklearn.svm import SVC
from sklearn import metrics


def SVM_Algorithm(Data):
    print ('Using SVM :-')
    print ('-------------')
   

    #Data Splitting :-
    x_train, x_test, y_train, y_test = Data

    #Data Training :-
    loan_model_svm = SVC(kernel = 'linear')
    loan_model_svm.fit(x_train,y_train)

    #Prediction for printing accuracy :-
    y_predict = loan_model_svm.predict(x_test)
    print('SVM accuracy for Loan Prediction = ',metrics.accuracy_score(y_predict,y_test))
    print("Y_Predicted : ",y_predict)


def SVM_Predictor(Data,features):    
    print ('Using SVM :-')
    print ('-------------')
   

    #Data Splitting :-
    x_train, x_test, y_train, y_test = Data

    #Data Training :-
    loan_model = SVC(kernel = 'linear')
    loan_model.fit(x_train,y_train)
    
    #Prediction for features :-
    predicted_val = loan_model.predict(features)
    print("Prediction for loan : ",predicted_val)
