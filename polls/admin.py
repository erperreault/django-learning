from django.contrib import admin

from .models import Question

# This gives Question objects an admin interface
admin.site.register(Question)
