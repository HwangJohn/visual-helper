# from django.conf.urls import url
from django.urls import path
from . import views
 
urlpatterns = [
    path('/predict', views.ImageCaptioning.as_view()),
]

