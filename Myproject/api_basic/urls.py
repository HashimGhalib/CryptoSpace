from django.urls import path
from .views import Home, Team, About, Service, Why, SignUp
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('service/', Service.as_view(), name='service'),
    path('team/', Team.as_view(), name='team'),
    path('why/', Why.as_view(), name='why'),

    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='finexo-html/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='finexo-html/logout.html'), name='logout')

]


