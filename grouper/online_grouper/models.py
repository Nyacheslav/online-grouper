from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from .validators import validate_file_extension
from django.contrib import admin


class SignalAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class Signal(models.Model):
    file = models.FileField(verbose_name='Файл',
                            upload_to='signals/',
                            validators=[validate_file_extension])
    delta = models.FloatField(verbose_name='Дельта')
    measurement = models.ForeignKey('Measurement',
                                    related_name='signals',
                                    on_delete=models.CASCADE,
                                    verbose_name='Измерение')

    def __str__(self):
        return f"Сигнал {self.pk}"

    class Meta:
        verbose_name = 'Сигнал'
        verbose_name_plural = 'Сигналы'


class GroupExaminationAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class GroupExamination(models.Model):
    examination = models.ForeignKey('Examination',
                                    related_name='group_examinations',
                                    on_delete=models.CASCADE,
                                    verbose_name='Обследование')
    group = models.ForeignKey('Group',
                              related_name='group_examinations',
                              on_delete=models.CASCADE,
                              verbose_name='Группа')

    def __str__(self):
        return f"Запись {self.pk}"

    class Meta:
        verbose_name = 'Запись об обследованиях группы'
        verbose_name_plural = 'Записи об обследованиях группы'


class GroupAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class Group(models.Model):
    name = models.CharField(max_length=80,
                            verbose_name='Название')
    description = models.CharField(max_length=300,
                                   verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class ExaminationAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class Examination(models.Model):
    name = models.CharField(max_length=80,
                            verbose_name='Имя')
    diagnosis = models.CharField(max_length=150,
                                 verbose_name='Диагноз')
    age = models.IntegerField(verbose_name='Возраст')
    gender = models.CharField(max_length=20,
                              verbose_name='Пол')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обследование'
        verbose_name_plural = 'Обследования'


class MeasurementAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class Measurement(models.Model):
    examination = models.ForeignKey('Examination',
                                    related_name='measurements',
                                    on_delete=models.CASCADE,
                                    verbose_name='Обследование')
    date = models.DateField(default=timezone.now(),
                            verbose_name='Дата измерения')

    def __str__(self):
        return f"Измерение {self.pk}"

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
