from django.urls import path

from .views import *

app_name = "online_grouper"

urlpatterns = [
    path('examinations/', ExaminationView.as_view()),
    path('signals/', SignalView.as_view()),
    path('signals/<int:pk>/file/download', SignalFileDownloadView.as_view()),
    path('groups/', GroupView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('groups_examinations/', GroupExaminationView.as_view())
]
