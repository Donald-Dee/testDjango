# Register your models here.
from .models import Voetbalspelers
from django.contrib import admin
from .models import Post

admin.site.register(Voetbalspelers) 
admin.site.register(Post)
