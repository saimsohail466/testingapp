from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('posts/new', views.new_post, name='new_post'),
  path('posts/<int:id>/edit', views.update_post, name='update_post'),
]
