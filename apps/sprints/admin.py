from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Sprint)
admin.site.register(TaskSprint)
admin.site.register(TaskSprintUser)