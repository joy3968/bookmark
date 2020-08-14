from django.contrib import admin

# Bookmark 모델을 불러온다.
from .models import Bookmark

# 불러온 모델을 등록한다.
admin.site.register(Bookmark)
# Register your models here.
