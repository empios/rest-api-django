from django.contrib import admin
from .models import Movie
from .models import Ratings
from .models import Comments

# Register your models here.
admin.site.register(Movie)
admin.site.register(Ratings)
admin.site.register(Comments)
