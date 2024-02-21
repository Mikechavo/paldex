from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import create_team, fire_team_detail, add_to_fire_team, remove_pal_from_fire_team, delete_fire_team

urlpatterns = [
   path('login_user', views.login_user, name="login"),
   path('logout_user', views.logout_user, name="logout"),
   path('register_user', views.register_user, name="register_user"),
   path('create/', create_team, name='create_team'),
   
   path('add_to_fire_team/<int:pal_Name>/<int:fire_team_id>/', views.add_to_fire_team, name='add_to_fire_team'), 
   path('fire_team/<int:fire_team_id>/', views.fire_team_detail, name='fire_team_detail'),
   path('remove_pal_from_fire_team/<int:fire_team_id>/<int:pal_Name>/', views.remove_pal_from_fire_team, name='remove_pal_from_fire_team'),
   path('delete_fire_team/<int:fire_team_id>/', views.delete_fire_team, name='delete_fire_team'),
   

]


# Add this block only in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)