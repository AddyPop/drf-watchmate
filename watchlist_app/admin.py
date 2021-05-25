from django.contrib import admin
from watchlist_app.models import watchlist, streamplatform, review
from django.utils.html import format_html
import emoji
# Register your models here.

class watchlistAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created', 'active')
    list_display_links = ('title',)
    list_editable = ('active',)
    search_fields = ('title',)


class reviewAdmin(admin.ModelAdmin):
    list_display = ('watchlist','description', 'created', 'updated', 'rating')
    list_display_links = ('watchlist',)
    search_fields = ('watchlist',)

class stramplatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'website','about' )
    list_display_links = ('name', 'website')
    search_fields = ('name',)

admin.site.register(watchlist, watchlistAdmin)
admin.site.register(streamplatform, stramplatformAdmin)
admin.site.register(review)
