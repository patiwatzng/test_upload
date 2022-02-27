from typing import Sequence
from django.db.models import query
from django.shortcuts import render, redirect
from .models import ColdSymptom, AllergySymptom, MuscleSymptom

def HomePage(request):
    request.session["total"] = 0
    return render(request, 'formdiagnosis/homepage.html')

def ColdsDiagnosisPage(request, count, value):
    listtotal = []
    sumtotal = 0
    if count == 9:
        bypass = ColdSymptom.objects.get(Sequence=8)
        request.session[bypass.QuestionName] = value
        query_question = ColdSymptom.objects.all()
        for data in query_question:
            listtotal.append(request.session[data.QuestionName]) 
        for i in listtotal:
            if i == 1:
                sumtotal += i
        percentage = (sumtotal/8)*100
        return render(request, 'formdiagnosis/diagnosis_ans.html', context={"percent":percentage})
    question = ColdSymptom.objects.get(Sequence=count)
    NextSequence = question.Sequence
    if count > 1:
        SaveQuestion = ColdSymptom.objects.get(Sequence=count-1)
        request.session[SaveQuestion.QuestionName] = value
        print(SaveQuestion.QuestionName, request.session[SaveQuestion.QuestionName]) 
    return render(request, "formdiagnosis/colddiagnosis.html", context={"Question":question, "NextSequence":int(NextSequence)+1} )

def ColdsDiagnosisDisplay(request):
    return render(request, "formdiagnosis/diagnosis_ans.html")

def AllergyDiagnosisPage(request, count, value):
    listtotal = []
    sumtotal = 0
    if count == 9:
        bypass = AllergySymptom.objects.get(Sequence=8)
        request.session[bypass.QuestionName] = value
        query_question = AllergySymptom.objects.all()
        for data in query_question:
            listtotal.append(request.session[data.QuestionName]) 
        for i in listtotal:
            if i == 1:
                sumtotal += i
        percentage = (sumtotal/8)*100
        return render(request, 'formdiagnosis/diagnosis_ans_allergy.html', context={"percent":percentage})
    question = AllergySymptom.objects.get(Sequence=count)
    NextSequence = question.Sequence
    if count > 1:
        SaveQuestion = AllergySymptom.objects.get(Sequence=count-1)
        request.session[SaveQuestion.QuestionName] = value
        print(SaveQuestion.QuestionName, request.session[SaveQuestion.QuestionName]) 
    return render(request, "formdiagnosis/allergydiagnosis.html", context={"Question":question, "NextSequence":int(NextSequence)+1} )

def MusclePage(request, count, value):
    listtotal = []
    sumtotal = 0
    if count == 9:
        bypass = MuscleSymptom.objects.get(Sequence=8)
        request.session[bypass.QuestionName] = value
        query_question = MuscleSymptom.objects.all()
        for data in query_question:
            listtotal.append(request.session[data.QuestionName])
        for i in listtotal:
            if i == 1:
                sumtotal += i
        percentage = (sumtotal/8)*100
        return render(request, 'formdiagnosis/muscle_ans.html', context={"percent":percentage})
    question = MuscleSymptom.objects.get(Sequence=count)
    NextSequence = question.Sequence
    if count > 1:
        SaveQuestion = MuscleSymptom.objects.get(Sequence=count-1)
        request.session[SaveQuestion.QuestionName] = value
        print(SaveQuestion.QuestionName, request.session[SaveQuestion.QuestionName])
    return render(request, "formdiagnosis/muscle.html", context={"Question":question, "NextSequence":int(NextSequence)+1} )