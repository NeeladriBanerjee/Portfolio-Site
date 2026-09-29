from django.contrib import admin
from .models import Project, About, Research, Skill, Education, Certification, ProfileLink

admin.site.register(Project)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(ProfileLink)
admin.site.register(Research)