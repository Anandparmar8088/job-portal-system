from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Job, InterestedJob, companies
from .Serializer import jobserializers, InterestedJobSerializer ,companiesSerializer


# =========================================================
# JOB CRUD SECTION
# =========================================================

# Get all jobs
@api_view(['GET'])
def getjobs(request):
    jobs = Job.objects.all()
    serializer = jobserializers(jobs, many=True)
    return Response({
        "success": True,
        "jobs": serializer.data
    })


# Post (Add) a new job
@api_view(['POST'])
def Job_posting(request):
    new_job_serializer = jobserializers(data=request.data)
    
    if new_job_serializer.is_valid():
        new_job_serializer.save()
        return Response({
            "success": True,
            "job": new_job_serializer.data
        })
    else:
        return Response({
            "success": False,
            "message": new_job_serializer.errors,
        })


# Delete a job by ID
@api_view(['DELETE'])
def delete(request, id):
    Job.objects.filter(id=id).delete()
    return Response({
        "success": True,
        "message": f"Job with ID {id} deleted successfully"
    })


# =========================================================
# INTERESTED JOB SECTION
# =========================================================

# Add a job to Interested list
@api_view(['POST'])
def add_interested(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
        interested, created = InterestedJob.objects.get_or_create(job=job)
        
        if created:
            return Response({"success": True, "message": "Job added to interested"})
        else:
            return Response({"success": False, "message": "Already marked as interested"})
    
    except Job.DoesNotExist:
        return Response({"success": False, "message": "Job not found"}, status=404)


# Get all interested jobs (latest first)
@api_view(['GET'])
def get_interested(request):
    interested_jobs = InterestedJob.objects.all().order_by("-created_at")
    serializer = InterestedJobSerializer(interested_jobs, many=True)
    return Response({
        "success": True,
        "interested": serializer.data
    })


# Delete an interested job by ID
@api_view(['DELETE'])
def delete_int(request, id):
    InterestedJob.objects.filter(id=id).delete()
    return Response({
        "success": True,
        "message": f"Interested job with ID {id} deleted successfully"
    })



# views for the compnies   ----


@api_view(['GET'])
def getCompanies(request):
    company = companies.objects.all()
    companySerializers = companiesSerializer(company,many=True)
    return Response({
        "success":True,
        "data":companySerializers.data
    })
    
    
@api_view(['POST'])
def postCompanies(request):
    New_company = companiesSerializer(data =request.data)
    
    if New_company.is_valid():
        New_company.save()
        return Response({
            "success":True,
            "company":New_company.data
        })
    else:
        return Response({
            "success":False,
            "message":New_company.errors
        })
    
    
