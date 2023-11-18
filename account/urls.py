from django.urls import path
from .views import Register, UsersList, UserProfile , Login

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('user-list/',UsersList.as_view(), name='user-list'),
    path("profile/", UserProfile.as_view(), name="profile"),
    path('login/', Login.as_view(), name='login'),

]
