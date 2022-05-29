import Preprocessing
from sklearn.feature_selection import SelectPercentile,chi2
from sklearn.model_selection import train_test_split
import Logistic_Regression

def feature_selection_and_data_Splitting(loanDf):
    
    X = loanDf.iloc[:,1:11].values
    Y = loanDf.iloc[:,12].values
    
    fs = SelectPercentile(score_func=chi2,percentile=70)
    X = fs.fit_transform(X, Y)
    
    x_train, x_test, y_train, y_test = train_test_split(X, Y,random_state=44,test_size=0.1,shuffle=True)
    
    Data = x_train, x_test, y_train, y_test
    return Data

