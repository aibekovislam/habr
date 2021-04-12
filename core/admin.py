from django.contrib import admin
from .models import Article, Author, Article_image
# Register your models here.
admin.site.register(Author)
admin.site.register(Article_image)


class ArticleAdmin(admin.ModelAdmin):
	class Meta:
		model = Article


	list_display = ('title', 'author', 'views', 'is_active', 'update_at')
	list_editable = ('author',)
	ordering = ['title']
	list_filter = ['is_active', 'update_at']
	search_fields = ['title', 'text']


	fields = ('title', 'text', 'views', 'created_at', 'update_at')
	readonly_fields = ('views', 'created_at', 'update_at')

admin.site.register(Article, ArticleAdmin)