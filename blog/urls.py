from django.urls import path
from . import views

urlpatterns = [
    # go to view.by in blog
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
