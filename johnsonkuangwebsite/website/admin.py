from django.contrib import admin

from website.models import *
from blog.models import *
from image_cropping import ImageCroppingMixin

class VideoAdmin(admin.ModelAdmin):
    # The list display lets us control what is shown in the default persons table at Home > Website > Videos
    # info on displaying multiple entries comes from http://stackoverflow.com/questions/9164610/custom-columns-using-django-admin
    list_display = ('name', 'date', 'project')

    # default the sort order in table to descending order by date
    ordering = ('-date',)

class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('__str__',)

class ResumeEntryBasicInfoAdmin(admin.ModelAdmin):
    list_display = ('age', 'phone', 'language')

class ResumeEntryEducationAdmin(admin.ModelAdmin):
    list_display = ('school', 'degree', 'start_date', 'end_date')

class ResumeSkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percent')

class ResumeWorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'position')

class BannerAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

class AboutGalleryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('name',)

# Register your models here.
admin.site.register(ResumeEntryBasicInfo,ResumeEntryBasicInfoAdmin)
admin.site.register(ResumeEntryEducation,ResumeEntryEducationAdmin)
admin.site.register(ResumeSkill,ResumeSkillAdmin)
admin.site.register(ResumeWorkExperience,ResumeWorkExperienceAdmin)
admin.site.register(About_Gallery, AboutGalleryAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Image, ImageAdmin)

