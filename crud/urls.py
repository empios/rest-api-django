from django.urls import path

from . import views
from .views import movies_list, add_movie, add_comment, get_comments,get_comments_by_id

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', movies_list),
    path('add/<str:title>', add_movie),
    path('comment/<str:id>', get_comments_by_id),
    path('addcomment', add_comment),
    path('comments/', get_comments)
]
