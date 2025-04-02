from django.urls import path
from . import views # import views from the current (.) dir

urlpatterns = [
    # go to view.by in blog
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('test/', views.test, name='blog-test')
]
