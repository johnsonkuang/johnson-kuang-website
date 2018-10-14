#TODO update site map for entire site
from django.contrib.sitemaps import Sitemap

from blog.models import *

'''
The changefreq and priority attributes indicate the change frequency of your post pages and their 
relevance in your website (the maximum value is 1). The items() method returns the QuerySet of 
objects to include in this sitemap. 
'''

'''
Django comes with a sitemap framework, which allows you to generate sitemaps for your site dynamically. 
A sitemap is an XML file that tells search engines the pages of your website, their relevance, and how 
frequently they are updated. Using a sitemap, you will help crawlers that index your website's content.
'''

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated