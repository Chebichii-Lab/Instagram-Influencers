from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns=[
    url(r'^$',views.home,name='home'),
    url('register/',views.signup, name='registration'),
    url('login/', auth_views.LoginView.as_view(), name='login'),
    url('profile/', views.user_profile, name='profile'),
    url('profile_update/', views.profile_update, name='change_profile'),

]