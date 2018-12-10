from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login_user, name='login_user'),
    url(r'^logout/', views.logout_view, name='logout_user')
]