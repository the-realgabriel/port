from django.contrib import admin
from .models import Name, Body, About, GalleryMedia

# Register your models here.

admin.site.register(Name),

admin.site.register(Body),

admin.site.register(About),

admin.site.register(GalleryMedia)

class GalleryMediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'created_at')
    list_filter = ('media_type',)