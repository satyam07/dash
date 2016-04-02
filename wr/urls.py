from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name='Home'),
	url(r'^wr/view/(?P<slug>[^\.]+).html', views.view_post, name='view_blog_post'),
	url(r'^wr/category/(?P<slug>[^\.]+).html', views.view_category, name='view_blog_category'),
	]

