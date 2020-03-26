from django.urls import include, re_path,path
from django.conf import settings

from . import views
from django.contrib.auth import views as auth_view
from Landing.views import Landing
from Login.views import Inicio

app_name = 'Landing'
app_name = 'Inicio'
urlpatterns = [
    path('',views.Landing, name = 'Landing')
]