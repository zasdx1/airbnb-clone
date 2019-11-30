from django.contrib import admin
from . import models

# Register your models here.


"""
admin패널에서 유저를 보고싶어 User를 컨트롤한 클래스가 바로 아래 클래스가 될꺼야
데코레이터는 클래스 위에 있어야 작동이 됨

admin.site.register(models.User, CustomUserAdmin)
과 같은 코드
"""


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "gender", "language", "currency", "superhost")

