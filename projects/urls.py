from django.urls import path
from . import views
urlpatterns =[
    path("",views.index, name="index"),
    path("oders/",views.oders, name="oders"),
    path("Heatlth/",views.Health,name="Health"),
]