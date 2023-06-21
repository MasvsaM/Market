from django.urls import path
from .views import index, login, registro, contactanos
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',index, name="index"),
    path('registro/',registro, name="registro"),
    path('login/',LoginView.as_view(template_name="core/admin/login.html"), name="login"),
    path('logout/',LogoutView.as_view(template_name="core/index.html"), name="logout"),
    path('/',contactanos, name="contactanos"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)