from django.contrib import admin
from django.urls    import path, include
from mvApp        import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),

]