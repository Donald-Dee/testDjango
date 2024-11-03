# Register your models here.
from django.contrib import admin
from .models import Voetbalspelers
from .models import Post

admin.site.register(Voetbalspelers) 
admin.site.register(Post)
