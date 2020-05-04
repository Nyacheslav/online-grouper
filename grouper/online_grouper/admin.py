from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Measurement, MeasurementAdmin)
admin.site.register(Examination, ExaminationAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(GroupExamination, GroupExaminationAdmin)
admin.site.register(Signal, SignalAdmin)
