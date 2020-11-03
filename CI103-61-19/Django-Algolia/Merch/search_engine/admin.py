from django.contrib import admin
from .models import Tags, Memes
from .forms import MemesForm
from django.contrib.admin import ModelAdmin
# Register your models here.

class MemesAdmin(ModelAdmin):
        form = MemesForm

class TagsAdmin(ModelAdmin):
        model = Tags

admin.site.register(Memes, MemesAdmin)
admin.site.register(Tags, TagsAdmin)