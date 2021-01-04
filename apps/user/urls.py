from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('<int:id>', views.show, name="show"),
    path('create', views.create, name="create"),
    path('create/userinfo', views.create_userinfo, name="create_userinfo"),
    path('<int:id>/update', views.update, name="update"),
    path('<int:id>/delete', views.delete, name="delete"),
    path('create/activate', views.activate, name="activate"),
]