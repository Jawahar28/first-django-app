from django.contrib import admin
from bingo.models import User, Product

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['username','name','email']
    list_display = ['username','email']
    search_fields = ['name']


admin.site.register(Product)
