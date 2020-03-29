from django.urls import path
from . import views


urlpatterns = [
    path('sbm', views.page_index),
    path('m_h', views.montre_homme),
]