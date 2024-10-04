from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('ru',views.home2),
    path('resume',views.resum),
]
