from django.contrib import admin
from .models import *
import admin_thumbnails
# Register your models here.

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1
    
class ProductAdmin(admin.ModelAdmin):
    list_display= ('product_name','price','stock','category','modified_date','is_available')
    prepopulated_fields= {'slug':('product_name',)}
    inlines = [ProductGalleryInline]

class VariationAdmin(admin.ModelAdmin):
    list_display=('product','variation_category','variation_value','is_active')
    list_editable=('is_active',)
    list_filter = ('product','variation_category','variation_value')
    

admin.site.register(Product,ProductAdmin)
admin.site.register(Variation,VariationAdmin)

# from .models import ContactMessage
# class ContactMessageAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'message')

# admin.site.register(ContactMessage)


from django.contrib import admin
from .models import ContactMessage

admin.site.register(ContactMessage)