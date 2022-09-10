from django.contrib import admin
from .models import Cart,CartItem, Review
# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem)
class ReviewAdmin(admin.ModelAdmin):
    list_display =['id','user','product','rate','created_at']
    readonly_fields = ['created_at',]
admin.site.register(Review,ReviewAdmin)