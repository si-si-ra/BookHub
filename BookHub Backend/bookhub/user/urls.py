from django.urls import path
from .views import *
from .import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

  
    path('users/', CreateUserView.as_view(), name='create-user'),
    path('users/<int:pk>/', UserDetailsView.as_view(), name='user-details'),
    path('users/update/<int:pk>/', UpdateUserView.as_view(), name='update-user'),
    path('users/delete/<int:pk>/', DeleteUserView.as_view(), name='delete-user'),
    path('users/search/', UserSearchView.as_view(), name='user-search'),

     path('login/', LoginView.as_view(), name='login'),
    
]