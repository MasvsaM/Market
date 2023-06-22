from django.urls import path
from .views import index, login, registro, contactanos, ofertas, celulares, computacionper, celularesAndroid, celularesHauwei, computacioncomponentes, computaciongaming
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',index, name="index"),
    path('registro/',registro, name="registro"),
    path('login/',LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout/',LogoutView.as_view(template_name="core/index.html"), name="logout"),
    path('/',contactanos, name="contactanos"),
    path('ofertas/',ofertas, name="ofertas"),
    path('celulares/',celulares, name="celulares"),
    path('celularesAndroid/',celularesAndroid, name="celularesAndroid"),
    path('celularesHauwei/',celularesHauwei, name="celularesHauwei"),
    path('computacionperifericos/',computacionper, name="computacionperifericos"),
    path('computacioncomponentes/',computacioncomponentes, name="computacioncomponentes"),
    path('computaciongaming/',computaciongaming, name="computaciongaming"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


