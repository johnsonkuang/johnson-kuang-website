from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


from django.urls import reverse
from taggit.managers import TaggableManager
from image_cropping import ImageRatioField
from website.models import *

from website.utils.fileutils import UniquePathAndRename

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()\
                          .filter(status='published')

class Post(models.Model):
    tags = TaggableManager()
    image = models.ImageField(blank=True, upload_to=UniquePathAndRename("blog/posts", True), max_length=255)

    cropping = ImageRatioField('image', '245x245', size_warning=True)
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # custom manager.
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    image_gallery = models.ManyToManyField(Image)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])

    def get_date_month_year(self):
        returnString = str(self.publish.day) + " " + self.publish.strftime('%B') + " | " + str(self.publish.year)
        return returnString

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def get_month_year(self):
        return self.created.strftime('%B %Y')

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


