from django.contrib import admin
from bingo.models import User, Product

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['name','email','age']
    list_display = ['name','email']
    search_fields = ['name']


admin.site.register(Product)
