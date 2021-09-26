from django.contrib import admin
from .models import Note, Tag, Deleted_Note, Deleted_Tag

admin.site.register(Note)
admin.site.register(Tag)
admin.site.register(Deleted_Note)
admin.site.register(Deleted_Tag)