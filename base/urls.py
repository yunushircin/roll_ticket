from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('category/', views.category, name='category'),
    path('alluser/', views.allUser, name='alluser'),

    path('add_problem/', views.createProblem, name="add_problem"),
    path('update_problem/<str:pk>', views.updateProblem, name="update_problem"),
    path('delete_category/<str:pk>', views.deleteCategory, name='delete_category'),
    path('notification/', views.notification, name='notification'),
    path('notification_read/<int:notification_id>/', views.notification_read, name='notification_read'),

    path('', views.home, name='home'),
    path('user/', views.userPage, name='user'),
]