from django.contrib import admin

# Register your models here.
# здесь регистрируются модели для их отображения в админ-панели
from test1.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)