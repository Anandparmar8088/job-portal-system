from django.db import models

class Job(models.Model):
    # poster = models.ImageField(upload_to="job_posters/", null=True, blank=True)
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    contact_info = models.EmailField()
    # created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
        return self.job_title
# This is interested button 
class InterestedJob(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="interested")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Interested: {self.job.job_title}"
    
    
    
    
# Rhis is for Companies button in Sidebar . 
class companies(models.Model):
    com_logo = models.URLField()
    com_name = models.TextField()
    com_culture = models.TextField()
    com_hq = models.TextField()
    com_ratings= models.IntegerField()
    com_website = models.URLField()
    
    
def __str__(self):
    return self.com_name
