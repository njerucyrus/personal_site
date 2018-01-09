from django.contrib import admin

# Register your models here.
from api.models import Skill, UserProfile

admin.site.register(Skill)
admin.site.register(UserProfile)
