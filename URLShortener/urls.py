'''
    If you meet any problems,
    please contact
    Leying Hu
    hu.leying@columbia.edu
'''
from django.urls import path

from . import views

app_name = 'URLShortener'
urlpatterns = [
    # '/URLShortener/'
    path('', views.index, name='index'),
    # '/URLShortener/5/'
    path('<int:urls_id>/', views.detail, name='detail'),
    path('image_upload', views.icon_image_view, name = 'image_upload'),
    path('success', views.success, name = 'success'),
]
