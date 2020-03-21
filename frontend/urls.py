from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name="index"),
    path('b/dashboard', views.dashboardView, name="dashboard"),
    path('logout/', views.logoutView, name="logout"),
    path('<str:smlr_url>', views.routeView, name="index"),
    # path('registration/', views.apiRegistration, name="api_registration"),
    path('login/', views.apiLogin, name="api_login"),
    path('getSmlr/', views.apigetSmlr, name="api_get_smlr"),
]