from django.urls import path
from .views import RegisterView, AuthLoginView, AuthLogoutView, UserListView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', AuthLoginView.as_view(), name='login'),
    path('logout/', AuthLogoutView.as_view(), name='logout'),
    path('users/', UserListView.as_view(), name='user_list'),
]
