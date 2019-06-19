from django.contrib import admin

# Register your models here.


from .models import *


class HeroInfoInlines(admin.StackedInline):
    """建立插入类"""
    model = HeroInfo
    extra = 3


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "price", "publisher", "isdeleted"]
    search_fields = ["id", "title", "author", "publisher"]
    list_filter = ["publisher"]


    fieldsets = [
        ("基本信息", {"fields": ["title", "author", "price", "publisher", "isDelete"]}),
        ("更多信息", {"fields": ["publish_date", "reading_volume", "comments"]})
    ]

    inlines = [HeroInfoInlines]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "hero_name", "hero_age", "hero_book", "isdeleted"]
    search_fields = ["id", "hero_name"]
    list_filter = []

    fieldsets = [
        ("基本信息", {"fields": ["hero_name", "hero_age", "hero_book", "isDelete"]}),
        ("更多信息", {"fields": ["hero_like", "hero_comments"]})
    ]



admin.site.register(BookInfo, BookInfoAdmin)

admin.site.register(HeroInfo, HeroInfoAdmin)