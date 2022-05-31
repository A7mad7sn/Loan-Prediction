#impoting Libraries :-
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics


def Decision_Tree_Algoithm(Data):
    print('Using Decision Tree Algorithm :-')
    print('---------------------------------')

    x_train, x_test, y_train, y_test = Data

    loan_Model = DecisionTreeClassifier(max_depth=2,random_state=6,splitter='best')
    loan_Model.fit(x_train, y_train)
    

    y_predict = loan_Model.predict(x_test)
    print('ID3 accuracy for Loan Prediction = ', metrics.accuracy_score(y_predict,y_test))
    print('Y_Real : ', y_test)
    print("Y_Predicted : ",y_predict)
   
    
def ID3_Predictor(Data,features):
    print('Using Decision Tree Algorithm :-')
    print('---------------------------------')
    
    x_train, x_test, y_train, y_test = Data

    loan_Model = DecisionTreeClassifier(max_depth=2,random_state=6,splitter='best')
    loan_Model.fit(x_train, y_train)
    
    #Prediction for features :-
    predicted_val = loan_Model.predict(features)
    print("Prediction for loan : ",predicted_val)

        