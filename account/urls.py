from django.urls import path
from account import views

urlpatterns=[
    path('resister',views.Resister,name="resister"),
    path('login',views.Login,name='login'),
    path('logout',views.Logout,name='logout'),
    path('delete',views.Delete,name='delete'),
]