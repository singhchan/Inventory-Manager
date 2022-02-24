from django.urls import path, include
from main import views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", login_required(views.profile), name='profile'),
    path("dashboard/<str:pk>", login_required(views.UserDashboard.as_view()), name='userdashboard'),
    path("update/", views.profile_update, name='profile_update'),
    path("try/", views.user_dashboard, name = 'try')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)