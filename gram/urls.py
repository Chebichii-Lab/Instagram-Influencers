from django.conf.urls import url
from . import views
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.home,name='home'),
    url('signup/', views.signup, name='signup'),
]