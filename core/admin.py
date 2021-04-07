from django.contrib import admin
from .models import Article, Author, Article_image
# Register your models here.
admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Article_image)