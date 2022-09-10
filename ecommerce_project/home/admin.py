from django.contrib import admin
from . models import category,products
# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name','slug')

admin.site.register(category,categoryAdmin)

class productAdmin(admin.ModelAdmin):
    list_display=['name','slug','categ','price','stock','img','available']
    list_editable=['price','stock','img','available']
    prepopulated_fields={'slug':('name',)}
admin.site.register(products,productAdmin)
