from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from cms.search.models import SearchKeyword

class SearchKeywordInline(admin.StackedInline):
    model = SearchKeyword
    extra = 1
    min_num = 3

class FlatPageAdmin(admin.ModelAdmin):
    model = FlatPage
    inlines = [SearchKeywordInline]

# Register your models here.
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
