from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_album, name='Add_Album'),
    path('edit/<int:id>/', views.edit_album, name='Edit_Album'),
    path('delete/<int:id>/', views.delete_album, name='Delete_Album'),
]