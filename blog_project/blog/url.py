from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.index, name='index_view'),
    path('post', views.post, name='post_view'),
    path('post/<slug:slug>', views.single_post, name='single_view'),


    
]