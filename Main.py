# imporing Modules
import Preprocessing
import Logistic_Regression
import Decision_Tree
import SVM

#Data Cleaning & Preprocessing :-
loan_Df = Preprocessing.Preprocessing()

#Calling Modules
Logistic_Regression.Logistic_algorirthm(loan_Df)
Decision_Tree.Decision_Tree(loan_Df)
SVM.svm_prediction(loan_Df)