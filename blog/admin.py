# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from blog import models

class NewsInfoAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'body',
                    'created_time',
                    'modified_time',
                    'excerpt',
                    'category',  
                    'author',
                    )
    search_fields = ('title', 'author')
    list_filter = ('created_time',)


admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Post,NewsInfoAdmin)
