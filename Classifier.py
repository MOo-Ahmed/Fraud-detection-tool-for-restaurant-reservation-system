import pandas as pd
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split 
from sklearn import metrics

from sklearn.tree import export_graphviz
from IPython.display import Image  
import pydotplus
import io

class Classifier :
    
    def __init__(self):
        self.filename = "reservations.csv"

    def run(self) :
        col_names = ['status', 'distance','name','gender','age','vacation']
        # load dataset
        df = pd.read_csv(self.filename)
        df = df.iloc[1:]
        feature_cols = ['distance','name','gender','age','vacation']
        X = df[feature_cols] # Features
        y = df['status'] # Target variable

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1) # 70% training and 30% test
        # Create Decision Tree classifer object
        clf = DecisionTreeClassifier()

        # Train Decision Tree Classifer
        clf = clf.fit(X_train,y_train)

        #Predict the response for test dataset
        y_pred = clf.predict(X_test)

        # Model Accuracy
        print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

        dot_data = io.StringIO()
        export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['0','1', '2'])
        graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
        graph.write_png('tree.png')
        Image(graph.create_png())
        print('finished')
