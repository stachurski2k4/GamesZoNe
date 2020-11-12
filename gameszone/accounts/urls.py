from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


app_name='accounts'

urlpatterns = [
  url(r'^admin/$',views.ProfileList.as_view(),name='list'),
  url(r'^login/$',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
  url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),
  url(r'^signup/$',views.signUp,name='signup'),
  url(r'^profile/(?P<pk>[-\w]+)/$',views.ProfileView.as_view(),name='profile'),
  url(r'^profile/(?P<pk>[-\w]+)/edit/$',views.editProfile,name='profile_edit'),
  url(r'^profile/(?P<pk>[-\w]+)/edit_pass/$',views.editPass,name='pass_edit'),
  url(r'^profile/(?P<pk>[-\w]+)/edit_level/$',views.EditLevel.as_view(),name='level_edit'),
]
