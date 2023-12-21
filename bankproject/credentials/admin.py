from django.contrib import admin
from credentials.models import UserProfile, District, Branch

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(District)
admin.site.register(Branch)
