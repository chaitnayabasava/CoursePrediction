from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index_student, name='index_student'),
    url(r'^reg_student/$',views.reg_student,name='reg_student'),
    url(r'^course_reg/$', views.course_reg, name='course_reg'), 
    url(r'^course_pred/$', views.course_prediction, name='course_pred'),  
    url(r'^course_poll/$', views.course_poll, name='course_poll'),      
]
