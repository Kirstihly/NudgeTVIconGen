'''
    If you meet any problems,
    please contact
    Leying Hu
    hu.leying@columbia.edu
'''
from django.contrib import admin

# Register your models here.
from .models import Urls, Shortener

class ShortenerInline(admin.StackedInline):
    model = Shortener
    extra = 0

class UrlsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields':['urls_text']}),
        ('Date Information', {'fields':['pub_date'], 'classes':['collapse']})
    ]
    inlines = [ShortenerInline]
    list_display = ('urls_text', 'pub_date')
    list_filter = ['pub_date']

admin.site.register(Urls, UrlsAdmin)
admin.site.register(Shortener)
