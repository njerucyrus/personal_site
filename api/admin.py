from django.contrib import admin

# Register your models here.
from api.models import Skill, UserProfile, Project

admin.site.register(Skill)
admin.site.register(UserProfile)
admin.site.register(Project)
