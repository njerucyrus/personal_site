from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^skills/$', views.SkillsView.as_view(),),
    url(r'^skills/(?P<pk>\d+)/$', views.SkillDetailView.as_view(),),
    url(r'^projects/$', views.ProjectsView.as_view(),),
    url(r'^projects/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(),),
    url(r'^users/$', views.UserView.as_view(),),
    url(r'^users/(?P<pk>\d+)/$', views.UserDetailView.as_view(),),
    url(r'^profiles/$', views.UserProfileView.as_view(),),
    url(r'^profiles/(?P<username>\w+)/$', views.UserProfileDetailView.as_view(),),
]