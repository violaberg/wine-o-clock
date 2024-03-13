from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import GalleryImage, Review, Contact
from django.urls import reverse
from django.http import HttpResponseRedirect

# Register your models here.
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'image_thumbnail']
    search_fields = ['description']
    list_per_page = 20
    actions = ['edit_selected_image']

    def image_thumbnail(self, obj):
        return '<img src="{}" width="50" height="50" />'.format(obj.image.url)

    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = 'Image'

    def edit_selected_image(self, request, queryset):
        if queryset.count() == 1:
            selected_id = queryset[0].id
            edit_url = reverse ('admin:wine_cellar_galleryimage_change', args=[selected_id])
            return HttpResponseRedirect(edit_url)
        else:
            self.message_user(request, 'Please select only one image to edit.', level='warning')
    
    edit_selected_image.short_description = 'Edit selected image'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        return super().change_view(request, object_id, form_url, extra_context)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)


admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(Review)
