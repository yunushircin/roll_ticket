from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('adduser/', views.addUser, name='adduser'),
    path('category/', views.category, name='category'),
    path('callcenter/<str:pk_test>/', views.callCenter, name='callcenter'),

    path('', views.home, name='home'),
    path('user/', views.userPage, name='user')
]