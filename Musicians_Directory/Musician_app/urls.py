from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_musician, name='Add_Musician'),
    path('edit/<int:id>/', views.edit_musician, name='Edit_Musician'),
    
]