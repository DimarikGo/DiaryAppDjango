from django.contrib import admin

from .models import *


class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'fio', 'birthday', 'city', 'AdrLive', 'mobile', 'created_at', 'email')


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'photo')


class WeekDayAdmin(admin.ModelAdmin):
    list_display = ('TimeVisit', 'DateVisit', 'patient')


admin.site.register(Patient, PatientAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Therapy)
admin.site.register(Formula)
admin.site.register(Exam)
admin.site.register(WeekDay, WeekDayAdmin)
