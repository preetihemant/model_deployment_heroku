import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Creata a dataframe with data from the csv file
path_in = './Iris.csv'
dataset = pd.read_csv(path_in)


# Input variables go into X and Y with the response variable
X= dataset.iloc[:,1:5]
Y= dataset.iloc[:,-1]

# initialize classifier 
clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=2, random_state=0)

# fit the data into the classifier model
clf.fit(X, Y)

#Save the model as a .pkl file
import pickle
with open('model.pkl', 'wb') as file:
    pickle.dump(clf, file)