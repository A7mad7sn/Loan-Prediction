#impoting Libraries :-
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

def Decision_Tree(Data):
    print ('------------------------------------------------------------------------')
    print('Using Decision Tree Algorithm :-')
    print('---------------------------------')

    x_train, x_test, y_train, y_test = Data

    loan_Model = DecisionTreeClassifier(max_depth=6,random_state=44)
    loan_Model.fit(x_train, y_train)
    
    y_predict = loan_Model.predict(x_test)
    print('ID3 accuracy for Loan Prediction = ', metrics.accuracy_score(y_predict,y_test))
    print("Prediction for Loan : ",y_predict)
    print ('------------------------------------------------------------------------')
   