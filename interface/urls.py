from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('upload/', views.upload_image, name='upload_image'),
    path('annoter/<int:image_id>/', views.annoter_image, name='annoter_image'),
    path('images/', views.liste_images, name='liste_images'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
