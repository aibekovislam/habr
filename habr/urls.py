from django.contrib import admin
from django.urls import path
from core.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path("articles/", articles, name='articles'),
    path("article/<int:id>/", article_page, name="article"),
    path('authors/', authors, name='authors'),
    path("article/<int:pk>/edit/", edit_article, name='articles_edit'),
    path("article_add/", add_article, name='news_home'),
    path("article/<int:id>/delete/", delete_article, name='delete_news' ),
    path("search/", search, name='search'),
    path("author/<int:pk>/", author, name="author"),
    path("login/", sign_in, name="login"),
    path("register", reg, name="reg"),
    path("account/", acc, name="account")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)