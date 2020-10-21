from django.contrib import admin
from .models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    list_display = ("text", "date_added")
    list_filter = ["date_added"]
    search_fields = ["text"]

admin.site.register(ToDo, ToDoAdmin)

# Register your models here.
