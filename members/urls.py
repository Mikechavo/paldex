from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import create_team, team_detail, add_to_fire_team

urlpatterns = [
   path('login_user', views.login_user, name="login"),
   path('logout_user', views.logout_user, name="logout"),
   path('register_user', views.register_user, name="register_user"),
   path('create/', create_team, name='create_team'),
   path('team/<int:team_id>/', team_detail, name='team_detail'),
   path('add_to_fire_team/<str:pal_name>/', views.add_to_fire_team, name='add_to_fire_team'), 
]


# Add this block only in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)