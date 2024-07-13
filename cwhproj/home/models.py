from django.db import models 

# Create your models here.

class Course(models.Model):
    category_list = {
        "FC":"FreeCourse", 
        "PC":"PremiumCourse"
    }
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    summary = models.TextField(blank=True)
    category = models.CharField(max_length= 2,choices=category_list)
    thumbnail = models.ImageField(upload_to="thumbnails")

    def __str__(self):
        return f"{self.title}-{self.category}"