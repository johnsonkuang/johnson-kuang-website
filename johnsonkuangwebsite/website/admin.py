from django.contrib import admin
from website.models import *

class VideoAdmin(admin.ModelAdmin):
    # The list display lets us control what is shown in the default persons table at Home > Website > Videos
    # info on displaying multiple entries comes from http://stackoverflow.com/questions/9164610/custom-columns-using-django-admin
    list_display = ('name', 'date', 'project')

    # default the sort order in table to descending order by date
    ordering = ('-date',)

# Register your models here.
admin.site.register(Video, VideoAdmin)
