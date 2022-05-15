#impoting Libraries :-
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

def Decision_Tree(loan_Df,features):
    print ('------------------------------------------------------------------------')
    print('Using Decision Tree Algorithm :-')
    print('---------------------------------')
    x = loan_Df[["Gender","Married","Dependents","Education","Self_Employed","ApplicantIncome","CoapplicantIncome","LoanAmount","Loan_Amount_Term","Credit_History","Property_Area"]].values
    y = loan_Df["Loan_Status"].values

    x_train, x_test, y_train, y_test = train_test_split(x, y)

    loan_Model = DecisionTreeClassifier()
    loan_Model.fit(x_train, y_train)
    
    y_predict = loan_Model.predict(x_test)
    print('ID3 accuracy for Loan Prediction = ', metrics.accuracy_score(y_predict,y_test))
    y_predict = loan_Model.predict(features)
    print("Prediction for Loan : ",y_predict)
    print ('------------------------------------------------------------------------')
   