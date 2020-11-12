from django.conf.urls import url
from . import views


app_name='games'

urlpatterns = [
    url(r'^$',views.GamesList.as_view(),name='list'),
    url(r'^add_game/$',views.gameAdd,name='game_add'),
    url(r'^(?P<pk>[-\w]+)/$',views.GameDetail.as_view(),name='game'),
    url(r'^(?P<pk>[-\w]+)/delete_game/$',views.DeleteGame.as_view(),name='game_delete'),
    url(r'^(?P<pk>[-\w]+)/edit_game/$',views.EditGame.as_view(),name='game_edit'),
    url(r'^(?P<pk>[-\w]+)/add_comment/$',views.addComment,name='comment_add'),
    url(r'^(?P<pk>[-\w]+)/add_image/$',views.addImage,name='image_add'),
    url(r'^(?P<pk>[-\w]+)/add_version/$',views.addVersion,name='version_add'),
    url(r'^delete_version/(?P<pk>\w+)/$',views.DeleteVersion.as_view(),name='delete_version'),

]