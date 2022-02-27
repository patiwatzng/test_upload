from django.contrib import admin
from .models import AllergySymptom, ColdSymptom, MuscleSymptom

admin.site.register(AllergySymptom)
admin.site.register(ColdSymptom)
admin.site.register(MuscleSymptom)