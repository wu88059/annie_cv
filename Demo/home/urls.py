from django.urls import path,include
from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('aboutme', views.aboutme, name="about me"),
    path('ob', views.ob, name="objectives"),
    path('ee', views.ee,name="E &E"),
    path('sc', views.sc, name="S&C"),
    
]