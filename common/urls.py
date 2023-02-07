from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import profile

app_name = 'common'

urlpatterns = [
    path('', views.index, name='main'),
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.detail, name='detail'), #마이페이지
    path('profile/', profile, name='user-profile'),
]