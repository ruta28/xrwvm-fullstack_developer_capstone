from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Render React login page
    path('login/', TemplateView.as_view(template_name="index.html")),

    # Login API
    path('loginuser/', views.login_user, name='login'),

    # Logout API
    path('logout/', views.logout_request, name='logout'),

    # Register API
    path('register/', views.registration, name='register'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)