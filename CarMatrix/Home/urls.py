from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('', views.signuppage, name='signup'),
    path('home/', views.home, name='home'),  





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
