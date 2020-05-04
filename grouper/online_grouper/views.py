from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.core.files.storage import default_storage
from .models import *
from .serializers import *
from django.http import HttpResponse


class ExaminationView(APIView):
    def get(self, request):
        examinations = Examination.objects.all()
        serializer = ExaminationSerializer(examinations, many=True)
        return Response({"examinations": serializer.data})


class MeasurementView(APIView):
    def get(self, request):
        measurements = Measurement.objects.all()
        serializer = MeasurementSerializer(measurements, many=True)
        return Response({"measurements": serializer.data})


class GroupView(APIView):
    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response({"groups": serializer.data})


class SignalView(APIView):
    def get(self, request):
        signals = Signal.objects.all()
        serializer = SignalSerializer(signals, many=True)
        return Response({"signals": serializer.data})


class GroupExaminationView(APIView):
    def get(self, request):
        groups_examinations = GroupExamination.objects.all()
        serializer = GroupExaminationSerializer(groups_examinations, many=True)
        return Response({"groups_examinations": serializer.data})


class SignalFileDownloadView(APIView):
    def get(self, request, pk):
        file = get_object_or_404(Signal, pk=pk)
        file_bin = default_storage.open(str(file.file), 'rb')
        file_data = file_bin.read()

        response = HttpResponse(file_data, content_type='application/file')
        response['Content-Disposition'] = f'attachment; filename="{file.file.name}"'
        return response
