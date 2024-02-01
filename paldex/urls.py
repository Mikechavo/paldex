# from django.urls import path
# from . import views

# urlpatterns = [
#   path("", views.home, name="home"),
#   path("todos/", views.todos, name="Todos")
# ]

# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    # ... other URL patterns ...
]

# Add this block only in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
