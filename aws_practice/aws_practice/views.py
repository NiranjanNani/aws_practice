from django.shortcuts import render
from . import predict_model

def home(request):
    return render(request,'index.html')


def result(request):
    Pclass=int(request.GET['PClass'])
    Age=int(request.GET['Age'])
    Sex=int(request.GET['Sex'])
    Fare=int(request.GET['Fare'])
    SibSp=int(request.GET['SibSp'])
    Parch=int(request.GET['Parch'])
    Title=int(request.GET['Title'])
    Embarked=int(request.GET['Embarked'])
    res=predict_model.predict_ml(Pclass,Age,Sex,SibSp,Parch,Fare,Embarked,Title)
    return render(request,'result.html',{'result':res})
