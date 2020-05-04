from rest_framework import serializers
from .models import *


class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = ['id', 'name', 'diagnosis', 'age', 'gender']


class SignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signal
        fields = ['id', 'delta', 'measurement', 'file']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'examination', 'date']


class GroupExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupExamination
        fields = ['id', 'group', 'examination']