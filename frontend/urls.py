from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name="index"),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('logout/', views.logoutView, name="logout"),
    path('<str:smlr_url>', views.routeView, name="index"),
]