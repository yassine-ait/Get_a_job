from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyRoutes.as_view(), name="routes"),

    path('offres/', views.OffresList.as_view(), name="offres"),

    path('postulesdisplay/',
         views.PostuleDisplay.as_view(), name="postulesdisplay"),

    path('offres/<str:pk>/',
         views.OffreView.as_view(), name="offre"),


    path('recruters/', views.RecrutersList.as_view(), name="recruters"),

    path('postules/', views.PostulesList.as_view(), name="postules"),



    #     path('postules/<str:pk>/<str:namec>',
    #          views.PostulesList.as_view(), name="postules"),


]
