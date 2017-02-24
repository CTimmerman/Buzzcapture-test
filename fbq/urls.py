from collection import views

urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^comments/$', views.comments, name='comments'),
]