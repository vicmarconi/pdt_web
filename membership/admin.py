from django.contrib import admin

from membership.models.member import Member


# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass