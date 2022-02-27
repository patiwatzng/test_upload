from django.db import models

class ColdSymptom(models.Model):
    Sequence = models.IntegerField(blank=True, null=True)
    Symptom = models.CharField(max_length=500, blank=True)
    QuestionName = models.CharField(max_length=500, blank=True)

class AllergySymptom(models.Model):
    Sequence = models.IntegerField(blank=True, null=True)
    Symptom = models.CharField(max_length=500, blank=True)
    QuestionName = models.CharField(max_length=500, blank=True)

class MuscleSymptom(models.Model):
    Sequence = models.IntegerField(blank=True, null=True)
    Symptom = models.CharField(max_length=500, blank=True)
    QuestionName = models.CharField(max_length=500, blank=True)

