from django.contrib import admin
from django.urls import path
from .views import HomePage, ColdsDiagnosisPage ,AllergyDiagnosisPage, MusclePage

urlpatterns = [
    path("", HomePage, name='home-page'),
    path("colddiagnosis/<int:count>/<int:value>/", ColdsDiagnosisPage, name="colddig-page"),
    path("allergydianosis/<int:count>/<int:value>/", AllergyDiagnosisPage, name="allergy-page"),
    path("muscle/<int:count>/<int:value>/", MusclePage, name="muscle-page")
]