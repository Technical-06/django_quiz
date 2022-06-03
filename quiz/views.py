import json
from django.http import HttpResponse, JsonResponse
from tkinter.messagebox import YES
from django.shortcuts import render
from quiz.models import Quiz
from django.core.serializers import serialize

# from .serializer import QuizSerializer
# from rest_framework.renderers import JSONRenderer

def HomePage(request):
    return render(request,"index.html")

def ques(request):
        quiz = Quiz.objects.all()
        return render(request,"ques.html",{"quiz":quiz})
    
        
   
def api(request):
    quiz = Quiz.objects.all()
    data=serialize('json',quiz,fields={'id','corrans'})
    return HttpResponse(data,content_type='application/json')

def getCorrectAnsResults(request):
    print("req received")
    userans=request.GET['userans']
    corrans=request.GET['corrans']
    print(userans,corrans)
    useranslist=json.loads(userans)
    corranslist=json.loads(corrans)
    score=0
    correct=0
    for i in range(len(useranslist)):
        if useranslist[i]==corranslist[i]:
            score+=1
            correct+=1   
    resultdict={'score':score,'right':correct,'percentage':(score/(len(corranslist)))*100}
    json_response=json.dumps(resultdict,indent=5)
    print("json response",json_response)
    return HttpResponse(json_response,content_type='application/json')


def thanks(request):
    return render(request,"thanks.html")