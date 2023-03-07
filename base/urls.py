from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('category/', views.category, name='category'),
    path('alluser/', views.allUser, name='alluser'),

    path('update_problem/<str:pk>', views.updateProblem, name="update_problem"),
    path('delete_category/<str:pk>', views.deleteCategory, name='delete_category'),

    path('', views.home, name='home'),
    path('user/', views.userPage, name='user'),
]