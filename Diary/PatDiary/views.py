import calendar
import datetime

from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from .forms import *
from .models import Patient, Exam, Formula, Photo, Therapy, WeekDay


def index(request):
    patient = Patient.objects.all()

    context = {
        "patient": patient,
    }
    return render(request, "patient.html", context)


def ViewCard(request, id):
    patient = Patient.objects.get(id=id)
    exam = Exam.objects.get(patient_id=id)
    formula = Formula.objects.get(patient_id=id)
    photo = Photo.objects.filter(patient_id=id)
    therapy = Therapy.objects.filter(patient_id=id)

    context = {
        "title": patient,
        "photo": photo,
        "formula": formula,
        "patient": patient,
        "exam": exam,
        "therapy": therapy,
    }
    return render(request, "Cardpat.html", context)


def Days(request):
    date_ch = request.POST.get('date_ch')
    weekday = WeekDay.objects.filter(DateVisit=date_ch)
    time = Timing()
    for i in weekday:
        time[i.TimeVisit] = i.patient
    time = time
    a = [date_ch]
    for date_str in a:
        y, m, d = date_str.split('-')
        day = int(d)
        month = int(m)
        year = int(y)
    WeeksDay = calendar.weekday(year, month, day)
    date = datetime.date(year, month, day)
    Day = DayWeeks(WeeksDay)

    context = {
        "date": date,
        "Day": Day,
        "time": time,

    }
    return render(request, "days.html", context)


# class CreatePatient(CreateView):
#     form_class = PatientForm
#     template_name = "AddPat.html"


def CreatePatient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            patient = Patient.objects.create(**form.cleaned_data)
            return redirect('CreateFormula', patient.pk)
    else:
        form = PatientForm()

    context = {
        'form': form,
    }
    return render(request, 'AddPat.html', context)


def CreateFormula(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        form = FormulaForm(request.POST)
        if form.is_valid():
            FormulaArray = form.cleaned_data
            FormulaArray['patient'] = patient
            Formula.objects.create(**FormulaArray)
            return redirect('CreateExam', patient.pk)
    else:
        form = FormulaForm()

    context = {
        'form': form,
        'patient': patient,
    }
    return render(request, 'AddFormula.html', context)


def CreateExam(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            ExamArray = form.cleaned_data
            print(ExamArray)
            ExamArray['patient'] = patient
            Exam.objects.create(**ExamArray)
            return redirect('CreatePhoto', patient.pk)
    else:
        form = ExamForm()
    context = {
        'form': form,
        'patient': patient,
    }
    return render(request, 'AddExam.html', context)


def CreatePhoto(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            PhotoArray = form.cleaned_data
            print(PhotoArray)
            PhotoArray['patient'] = patient
            Photo.objects.create(**PhotoArray)
            return redirect('Viewcard', patient.pk)
    else:
        form = PhotoForm()

    context = {
        'form': form,
        'patient': patient,
    }
    return render(request, 'AddPhoto.html', context)


def ViewPat(request, id):
    patient = Patient.objects.get(id=id)

    context = {
        "patient": patient,
    }
    return render(request, "AddPatView.html", context)


def DeletePat(request, id):
    try:
        patient = Patient.objects.filter(id=id)
        patient.delete()
        return redirect('/')
    except patient.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def WeekdayRe(request):
    if request.method == "POST":
        form = WeekDayForm(request.POST)
        if form.is_valid():
            WeekDay.objects.create(**form.cleaned_data)
            return redirect('/')

    else:
        form = WeekDayForm()
    context = {
        "form": form,
        # "weekday": weekday,
    }
    return render(request, "SavePat.html", context)


def EditFormula(request, id):
    patient = Patient.objects.get(id=id)
    formula = Formula.objects.get(patient_id=id)
    if request.method == 'POST':
        Formula.objects.get(patient_id=id).delete()
        form = FormulaForm(request.POST)
        if form.is_valid():
            FormulaArray = form.cleaned_data
            FormulaArray['patient'] = patient
            Formula.objects.create(**FormulaArray)
            return redirect('/')
    else:
        form = FormulaForm()
    context = {
        "form": form,
        "formula": formula,
        "patient": patient,
    }
    return render(request, "EditFormula.html", context)


def AnalizFormula(request, id):
    formula = Formula.objects.filter(patient_id=id)
    analiz = Analiz(id)
    print(analiz)
    context = {

        "formula": formula,
        # "analiz": analiz,

    }
    return render(request, "AnalizFormula.html", context)
