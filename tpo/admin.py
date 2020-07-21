from django.contrib import admin
from .models import CompanyProfile,Sector,Choices,Feedback,Profile,LeavePage
# Register your models here.
admin.site.register(CompanyProfile)
admin.site.register(Sector)
admin.site.register(Choices)
admin.site.register(Feedback)
admin.site.register(Profile)
admin.site.register(LeavePage)