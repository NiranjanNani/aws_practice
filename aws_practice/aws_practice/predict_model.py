import pickle



def predict_ml(Pclass,Age,Sex,SibSp,Parch,Fare,Embarked,Title):
    model=pickle.load(open('titanic_model.sav','rb'))
    x=[[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked,Title]]
    p=model.predict(x)
    if p==1:
        return "Survived"
    else:
        return "Not Survived"
