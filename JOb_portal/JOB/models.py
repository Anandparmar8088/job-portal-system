from django.db import models

class Job(models.Model):
    # poster = models.ImageField(upload_to="job_posters/", null=True, blank=True)
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    contact_info = models.EmailField()
    # created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
        return self.job_title