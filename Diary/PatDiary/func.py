from .models import Patient, Exam, Formula, Photo, Therapy, WeekDay



def DayWeeks(day):
    if day == 0:
        days = "Понедельник"
        return days
    elif day == 1:
        days = "Вторник"
        return days
    elif day == 2:
        days = "Среда"
        return days
    elif day == 3:
        days = "Четверг"
        return days
    elif day == 4:
        days = "Пятница"
        return days
    elif day == 5:
        days = "Суббота"
        return days
    elif day == 6:
        days = "Воскресенье"
        return days


def Timing():
    n = ' '
    dicts = {'8-00': n, '8-30': n, '9-00': n, '9-30': n, '10-00': n, '10-30': n, '11-00': n, '11-30': n, '12-00': n,
             '12-30': n, '13-00': n, '13-30': n, '14-00': n, '14-30': n, '15-00': n, '15-30': n, '16-00': n, '16-30': n,
             '17-00': n, '17-30': n, '18-00': n, '18-30': n,
             '19-00': n, '19-30': n}
    return dicts


def Analiz(id):
    formula = Formula.objects.filter(patient_id=id).values()
    print(formula)
