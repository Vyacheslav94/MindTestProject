from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('personal', views.personal, name="personal"),
    path('creation_test', views.creation_test, name="creation_test"),
    path('creation', views.creation, name="creation"),
    path('library', views.library, name="library")
]