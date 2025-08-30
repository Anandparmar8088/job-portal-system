from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Job
from .Serializer import jobserializers

@api_view(['GET'])
def getjobs(request):
    job =Job.objects.all()
    serializer = jobserializers(job, many=True)
    return Response({
        "success":True,
        "jobs":serializer.data
    })
    
    
    
    
    
    
    
@api_view(['POST'])
def Job_posting(request):
    # print("in cominging data ",request.data)
    new_job_serializers = jobserializers(data=request.data)
    
    if new_job_serializers.is_valid():
        new_job_serializers.save()
        return Response({
            "success":True,
            "job":new_job_serializers.data
            
        })
    else:
        return Response({
            "success":False,
            "Message":new_job_serializers.errors,
           
        })
   