from django.db import models


class Exam(models.Model):
    complaints = models.CharField(max_length=150, blank=True, null=True, verbose_name='Жалобы')
    anamnes = models.CharField(max_length=150, blank=True, null=True, verbose_name='Анамнез')
    StLocalis = models.CharField(max_length=150, blank=True, null=True, verbose_name='Общий осмотр')
    PreDiagnose = models.CharField(max_length=150, blank=True, null=True, verbose_name='Предварительный диагноз')
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.patient)

    class Meta:
        verbose_name = 'Обследование'
        verbose_name_plural = 'Обследования'


class Therapy(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата лечения')
    treatment = models.TextField(max_length=400, blank=True)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, null=True, verbose_name='Пациент')

    def __str__(self):
        return str(self.patient)

    class Meta:
        verbose_name = 'Лечение'
        verbose_name_plural = 'Лечения'
        ordering = ['-created_at']


class Formula(models.Model):
    N = ''
    Caries = 'Ca'
    Pulpit = 'P'
    Periodontit = 'Pt'
    EXTRACT = 'EX'
    CROWN = 'Cd'
    ARTTOOTH = 'Ar'
    DIAG_CHOICES = [
        (N, ''),
        (Caries, 'C'),
        (Pulpit, 'P'),
        (Periodontit, 'Pt'),
        (EXTRACT, 'A'),
        (CROWN, 'Cd'),
        (ARTTOOTH, 'Ar')
    ]
    tooth18 = models.CharField(verbose_name="18", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth17 = models.CharField(verbose_name="17", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth16 = models.CharField(verbose_name="16", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth15 = models.CharField(verbose_name="15", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth14 = models.CharField(verbose_name="14", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth13 = models.CharField(verbose_name="13", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth12 = models.CharField(verbose_name="12", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth11 = models.CharField(verbose_name="11", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth21 = models.CharField(verbose_name="21", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth22 = models.CharField(verbose_name="22", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth23 = models.CharField(verbose_name="23", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth24 = models.CharField(verbose_name="24", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth25 = models.CharField(verbose_name="25", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth26 = models.CharField(verbose_name="26", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth27 = models.CharField(verbose_name="27", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth28 = models.CharField(verbose_name="28", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth38 = models.CharField(verbose_name="38", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth37 = models.CharField(verbose_name="37", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth36 = models.CharField(verbose_name="36", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth35 = models.CharField(verbose_name="35", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth34 = models.CharField(verbose_name="34", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth33 = models.CharField(verbose_name="33", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth32 = models.CharField(verbose_name="32", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth31 = models.CharField(verbose_name="31", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth41 = models.CharField(verbose_name="41", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth42 = models.CharField(verbose_name="42", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth43 = models.CharField(verbose_name="43", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth44 = models.CharField(verbose_name="44", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth45 = models.CharField(verbose_name="45", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth46 = models.CharField(verbose_name="46", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth47 = models.CharField(verbose_name="47", blank=True, max_length=20, choices=DIAG_CHOICES)
    tooth48 = models.CharField(verbose_name="48", blank=True, max_length=20, choices=DIAG_CHOICES)
    patient = models.OneToOneField('Patient', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.patient)

    class Meta:
        verbose_name = 'Формула зубов'
        verbose_name_plural = 'Формулы зубов'


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.patient)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class WeekDay(models.Model):
    DateVisit = models.DateField(verbose_name='День записи', null=True, blank=True)
    TimeVisit = models.CharField(max_length=20, verbose_name='Время записи', null=True, blank=True)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, verbose_name='Пациент')

    def __str__(self):
        return str(self.patient)

    class Meta:
        verbose_name = 'Дата записи'
        verbose_name_plural = 'Даты записи'
        ordering = ['DateVisit', 'TimeVisit']


class Patient(models.Model):
    fio = models.CharField(max_length=150, blank=True)
    birthday = models.DateField()
    city = models.CharField(max_length=50, blank=True)
    AdrLive = models.CharField(max_length=150, blank=True)
    mobile = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        ordering = ['-created_at']
