from django.urls import path
from .views import *
urlpatterns = [
    path('',Home.as_view(),name='userhome'),
    path('about/',About.as_view(),name='userabout'),
    path('whyus/',WhyUs.as_view(),name='userwhyus'),
    path('clients/',ClientsView.as_view(),name='userclients'),
    path('gallery/',Gallery.as_view(),name='usergallery'),
    path('booknow/',BookNow.as_view(),name='booknow'),
    path('planning&development/',PlanningDevelopment.as_view(),name='planning'),
    path('customerexperince/',CustomerExperiece.as_view(),name='customerexperince'),
    path('operation&management/',OperationManagement.as_view(),name='operationmanagement'),
    path('human_resources/',HumanResources.as_view(),name='humanresource'),
    path('wellness&recreational_consulting/',Wellness.as_view(),name='wellness'),
    path('food&beverageconsulting/',Foodbev.as_view(),name='foodbev'),

]