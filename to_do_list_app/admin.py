from django.contrib import admin

# Register your models here.
from to_do_list_app.models import Tags, Task

admin.site.register(Tags)
admin.site.register(Task)