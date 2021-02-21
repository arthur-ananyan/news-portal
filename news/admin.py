from django.contrib import admin
from .models import Category, News, MainCategory
from django.utils.html import format_html

admin.site.register(Category)
admin.site.register(MainCategory)


@admin.register(News)
class NewsAdminModel(admin.ModelAdmin):
    list_display = ['main_category',
                    'news_title', 'text', 'creation_date']
    list_filter = ('category', "creation_date")

    def text(self, obj):
        return format_html(obj.news_text)
