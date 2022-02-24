from django.urls import path, include
from authen import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login', views.Login.as_view(), name='login'),
    path('logout', login_required(views.Logout.as_view(), login_url='login'), name = 'logout'),
    path('register', views.register, name='register'),
    path('', include('main.urls'))
]