from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='Main'),
    path('card-pat/<int:id>/', ViewCard, name='Viewcard'),
    path('days/', Days, name="Days"),
    # path('add-pat', CreatePatient.as_view(), name='CreatePatient'),
    path('add-pat/', CreatePatient, name='CreatePatient'),
    path('add-form/<int:id>/', CreateFormula, name="CreateFormula"),
    path('add-exam/<int:id>/', CreateExam, name="CreateExam"),
    path('add-photo/<int:id>/', CreatePhoto, name='CreatePhoto'),
    path('view-pat/<int:id>/', ViewPat, name='ViewPat'),
    path('del/<int:id>/', DeletePat, name='DeletePat'),
    path('day/', WeekdayRe, name="WeekdayRe"),
    path('edit-formula/<int:id>/', EditFormula, name="EditFormula"),
    path('analiz-formula/<int:id>/', AnalizFormula, name="AnalizFormula")

]
