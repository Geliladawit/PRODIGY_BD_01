from django.urls import path
from .views import read, update, delete, create,userlist

urlpatterns = [
    path('users/', userlist, name='user_list'),
    path('users/<str:user_id>/read/', read, name='read_user'),
    path('users/<str:user_id>/update/', update, name='update_user'),
    path('users/<str:user_id>/delete/', delete, name='delete_user'),
    path('users/create/', create, name='create_user'),
]
