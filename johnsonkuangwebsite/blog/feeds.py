from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import *

class LatestPostsFeed(Feed):
    title = 'Johnson\'s Corner of the Internet'
    link = '/blog/'
    description = 'New posts of my blog.'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)