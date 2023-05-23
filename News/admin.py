from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "reporter"]
    prepopulated_fields = {'slug':('title',)}


admin.site.register(News, NewsAdmin)
