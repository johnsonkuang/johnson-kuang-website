from django.db import models

from website.utils.fileutils import UniquePathAndRename

# Create your models here.
class Banner(models.Model):
    image = models.ImageField(blank=True, upload_to=UniquePathAndRename('banner', True), max_length=255)

class Video(models.Model):
    name = models.CharField(max_length=500)
    video = models.FileField(verbose_name='static_videos', upload_to='videos/')

    #Separation of videos by page they are to be loaded with for future filtering
    INDEX = "Index"
    ABOUT = "About"
    RESUME = "Resume"
    VACATION = "Vacation"
    PROJECTS = "Projects"
    SANDBOX = "Sandbox"
    
    PAGE_CHOICES = (
        (INDEX, INDEX),
        (ABOUT, ABOUT),
        (RESUME, RESUME),
        (VACATION, VACATION),
        (PROJECTS, PROJECTS),
        (SANDBOX, SANDBOX),
    )

    page = models.CharField(max_length=50, choices = PAGE_CHOICES, null=True)

    def __str__(self):
        return self.name + ": " + str(self.video)