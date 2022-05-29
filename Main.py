# imporing Modules
import Preprocessing
import Feature_Selection_Splitting
import Logistic_Regression
import Decision_Tree
import SVM

#Data Cleaning & Preprocessing & Data Scaling :-
loan_Df = Preprocessing.Preprocessing()
#Feature Selection & Data Splitting :-
ReadyData = Feature_Selection_Splitting.feature_selection_and_data_Splitting(loan_Df)
#Calling Modules  :-
Logistic_Regression.Logistic_algorirthm(ReadyData)
Decision_Tree.Decision_Tree(ReadyData)
SVM.svm_prediction(ReadyData)