from django.contrib import admin
from coltrane.models import Category, CategoryAdmin, Entry, EntryAdmin, Link, LinkAdmin


admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Link, LinkAdmin)