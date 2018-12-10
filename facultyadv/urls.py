from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.posts_page, name='posts_page'),
    url(r'^applications', views.index, name='index'), 
    
        

    url(r'^posts/', views.posts_page, name='posts_page'),
    url(r'^post_details/(?P<rule_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^del_posts/(?P<rule_id>[0-9]+)/$', views.del_post, name='del_post'),        
        
    url(r'^$', views.index, name='index'),
    url(r'^approve/(?P<student_id>[0-9]+)/$',views.approve,name='approve'),
    url(r'^disapprove/(?P<student_id>[0-9]+)/$',views.approve,name='disapprove'),
]
