from django.contrib import admin
from .models import (
    Profile,
    Experience,
    Project,
    Certificate,
    TechnicalSkill,
    SoftSkill,
    Links
)

# Register each model so it shows up in admin panel
admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Certificate)
admin.site.register(TechnicalSkill)
admin.site.register(SoftSkill)
admin.site.register(Links)
