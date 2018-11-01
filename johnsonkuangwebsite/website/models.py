from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete, post_delete, pre_save, post_save, m2m_changed
from django.utils import timezone
from django.contrib.auth.models import User

from datetime import date

from image_cropping import ImageRatioField
from sortedm2m.fields import SortedManyToManyField
from website.utils.fileutils import UniquePathAndRename


class Project(models.Model):
    name = models.CharField(max_length=255)

    #short name for urls
    short_name = models.CharField(max_length=255)
    short_name.help_text = "This should be the same as the name but lower case with no spaces or special characters"

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    gallery_image = models.ImageField(upload_to='projects/images', blank=True, null=True, max_length=255)
    cropping = ImageRatioField('gallery_image', '500x400', size_warning=True)

    about = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.short_name = ''.join(e for e in self.name.lower() if e.isalnum())
        super(Project, self).save(*args, **kwargs)


class Banner(models.Model):
    # Separation of videos by page they are to be loaded with for future filtering
    INDEX = "Index"
    ABOUT = "About"
    RESUME = "Resume"
    VACATION = "Vacation"
    PROJECTS = "Projects"
    IND_PROJECT = "Individual Project"
    SANDBOX = "Sandbox"

    PAGE_CHOICES = (
        (INDEX, INDEX),
        (ABOUT, ABOUT),
        (RESUME, RESUME),
        (VACATION, VACATION),
        (PROJECTS, PROJECTS),
        (IND_PROJECT, IND_PROJECT),
        (SANDBOX, SANDBOX),
    )

    page = models.CharField(max_length=50, choices=PAGE_CHOICES, default=INDEX)
    image = models.ImageField(blank=True, upload_to=UniquePathAndRename('banner', True), max_length=255)

    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)
    project.help_text = "If this banner is attached to a specific project, set page to IND_Project"

    cropping = ImageRatioField('image', '2000x500', free_crop=True)
    image.help_text = 'You must select "Save and continue editing" at the bottom of the page after uploading a new image for cropping. Please note that since we are using a responsive design with fixed height banners, your selected image may appear differently on various screens.'
    title = models.CharField(max_length=50, blank=True, null=True)
    caption = models.CharField(max_length=1024, blank=True, null=True)
    alt_text = models.CharField(max_length=1024, blank=True, null=True)
    link = models.CharField(max_length=1024, blank=True, null=True)
    favorite = models.BooleanField(default=False)
    favorite.help_text = 'Check this box if this image should appear before other (non-favorite) banner images on the same page.'
    date_added = models.DateField(auto_now=True)

    def admin_thumbnail(self):
        if self.image:
            return u'<img src="%s" height="100"/>' % (self.image.url)
        else:
            return "No image found"

    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True

    def __str__(self):
        if self.title and self.page:
            return self.title + ' (' + self.get_page_display() + ')'
        else:
            return "Banner object for " + self.get_page_display()

'''
TODO: Get this to work 
@receiver(pre_delete, signal=Banner)
def banner_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(True)
'''

class Image(models.Model):
    image = models.ImageField(upload_to='images/', max_length=255)
    caption = models.CharField(max_length=255, blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL)
    image.help_text = 'You must select "Save and continue editing" at the bottom of the page after uploading a new image for cropping. Please note that since we are using a responsive design with fixed height banners, your selected image may appear differently on various screens.'

    # Copied from person model
    # LS: Added image cropping to fixed ratio
    # See https://github.com/jonasundderwolf/django-image-cropping
    # size is "width x height"

    def __str__(self):
        return self.caption


class Video(models.Model):
    name = models.CharField(max_length=500)
    video = models.FileField(verbose_name='static_videos', upload_to='videos/')
    date = models.DateField(null=True)

    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL)

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


class ResumeEntryEducation(models.Model):
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    degree_specific = models.CharField(max_length=255, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def is_Present(self):
        return self.end_date > date.today()

class ResumeEntryBasicInfo(models.Model):
    #Meant to store all basic info in one entry
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    about_description = models.TextField()

class ResumeSkill(models.Model):
    name = models.CharField(max_length=255)
    percent = models.IntegerField()
    percent.help_text = 'You must choose an int between 0 and 100 representing precentage'

class ResumeWorkExperience(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    position = models.CharField(max_length=255)
    description = models.TextField()

    def get_Start_Month(self):
        return self.start_date.strftime("%B")

    def get_End_Month(self):
        return self.end_date.strftime("%B")

    def is_Present(self):
        return self.end_date > date.today()



