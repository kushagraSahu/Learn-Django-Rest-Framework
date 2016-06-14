from django.conf.urls import url, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^$', views.api_root),
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    url(r'^user/$', views.UserList.as_view(), name='user-list'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)

# Login and logout views for the browsable API
urlpatterns += [
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]