from django import forms
from django.forms import ModelForm

from .models import Formula, Patient, Exam, Photo
from .func import *


class PatientForm(forms.Form):
    fio = forms.CharField(max_length=50, label='Фамилия Имя Отчество',
                          widget=forms.TextInput(attrs={"class": "form-control"}))
    birthday = forms.DateField(label='Дата рождения', required=False,
                               widget=forms.DateInput(attrs={"class": "form-control",
                                                             "type": "date", }))
    city = forms.CharField(max_length=50, label='Город',
                           widget=forms.TextInput(attrs={"class": "form-control", })
                           )
    AdrLive = forms.CharField(max_length=150, label='Адрес проживания',
                              widget=forms.TextInput(attrs={"class": "form-control", })
                              )
    mobile = forms.CharField(max_length=50, label='Номер телефона',
                             widget=forms.TextInput(attrs={"class": "form-control", })
                             )
    email = forms.EmailField(max_length=150, label='Email',
                             widget=forms.EmailInput(attrs={"class": "form-control", })
                             )


class FormulaForm(ModelForm):
    class Meta:
        model = Formula
        fields = '__all__'


class ExamForm(forms.Form):
    complaints = forms.CharField(max_length=50, label='Жалобы',
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    anamnes = forms.CharField(max_length=50, label='Анамнез',
                              widget=forms.TextInput(attrs={"class": "form-control"}))
    StLocalis = forms.CharField(max_length=200, label='Общий осмотр',
                                widget=forms.TextInput(attrs={"class": "form-control",
                                                              "rows": "5"}))
    PreDiagnose = forms.CharField(max_length=50, label='Предварительный диагноз',
                                  widget=forms.TextInput(attrs={"class": "form-control"}))


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'


TIME_CHOICES = [('8-00', '8-00'),
                ('8-30', '8-30'),
                ('9-00', '9-00'),
                ('9-30', '9-30'),
                ('10-00', '10-00'),
                ('10-30', '11-30'),
                ('11-00', '11-00'),
                ('11-30', '11-30'),
                ('12-00', '12-00'),
                ('12-30', '12-30'),
                ('13-00', '13-00'),
                ('13-30', '13-30'),
                ('14-00', '14-00'),
                ('14-30', '14-30'),
                ('15-00', '15-00'),
                ('15-30', '15-30'),
                ('16-00', '16-00'),
                ('16-30', '16-30'),
                ('17-00', '17-00'),
                ('17-30', '17-30'),
                ('18-00', '18-00'),
                ('18-30', '18-30'),
                ('19-00', '19-00'),
                ('19-30', '19-30'),
                ]


class WeekDayForm(forms.Form):
    DateVisit = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control",
                                                              "type": "date",
                                                              "class": "p-3 border bg-light",
                                                              "class": "col-2"}),
                                label="Дата визита")
    TimeVisit = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control",
                                                             "class": "col-2",
                                                             "class": "p-2 border bg-light"}),
                                  choices=TIME_CHOICES,
                                  label="Время записи")
    patient = forms.ModelChoiceField(widget=forms.Select(attrs={"class": "form-control",
                                                                "class": "col-4",
                                                                "class": "p-2 border bg-light"}),
                                     queryset=Patient.objects.all(),
                                     label="Пациент")
