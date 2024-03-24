from django.urls import path
from . import views

urlpatterns = [
    path('', views.slideshow, name='slideshow'),
    path('image/<int:image_id>/', views.image_detail, name='image_detail'),
    path('upload/', views.upload_presentation, name='upload_presentation'),
]
