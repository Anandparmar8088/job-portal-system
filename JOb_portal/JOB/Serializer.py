from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Job,InterestedJob,companies

class jobserializers(ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class InterestedJobSerializer(serializers.ModelSerializer):
    job = jobserializers(read_only=True)

    class Meta:
        model = InterestedJob
        fields = "__all__"


class companiesSerializer(ModelSerializer):
    class Meta:
        model = companies
        fields = "__all__"

       