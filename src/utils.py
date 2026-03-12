import os
import pickle
from sklearn.metrics import accuracy_score

def save_object(file_path,obj):

    dir_path=os.path.dirname(file_path)

    os.makedirs(dir_path,exist_ok=True)

    with open(file_path,"wb") as file_obj:

        pickle.dump(obj,file_obj)


def load_object(file_path):

    with open(file_path,"rb") as file_obj:

        return pickle.load(file_obj)


def evaluate_models(X_train,y_train,X_test,y_test,models):

    report={}

    for name,model in models.items():

        model.fit(X_train,y_train)

        y_pred=model.predict(X_test)

        score=accuracy_score(y_test,y_pred)

        report[name]=score

    return report

