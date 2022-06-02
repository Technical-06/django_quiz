import json
from django.http import HttpResponse, JsonResponse
from tkinter.messagebox import YES
from django.shortcuts import render
from quiz.models import Quiz
# from .serializer import QuizSerializer
# from rest_framework.renderers import JSONRenderer

def HomePage(request):
    return render(request,"index.html")

def ques(request):
    quiz = Quiz.objects.all()
    return render(request,"ques.html",{"quiz":quiz})
    # quiz = Quiz.objects.all()
    # serializer=QuizSerializer(quiz,many=True)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')



def results(request):
    score=0
    user_ans=[]
    for i in range(1,6):
        user_ans.append(request.POST[str(i)])
    quiz = Quiz.objects.all()
    corr_ans=[]
    for i in quiz:
     corr_ans.append(i.corrans)   
    for i in range(5):
        if user_ans[i]==corr_ans[i]:
            score += 1
    remarks=""
    if ((score/5) *100)<60:
        remarks="fail"
    else:
        remarks="pass"
    return render(request,"results.html",{"score":score,"remarks":remarks,"percentage":(score)/5*100},)

def thanks(request):
    return render(request,"thanks.html")