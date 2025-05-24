from django.contrib import admin
from .models import Member, MemberDetails, User

# Register your models here.

admin.site.register(Member)
admin.site.register(MemberDetails)
#admin.site.register(User)
#admin.site.register(LoyaltyProgram)