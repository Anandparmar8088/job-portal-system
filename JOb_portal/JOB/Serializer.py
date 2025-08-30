from rest_framework.serializers import ModelSerializer

from .models import Job

class jobserializers(ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

