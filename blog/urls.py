from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='post_list'),

    url(r'^about$', views.about, name='about'),
    url(r'^book$', views.post_list, name='book'),
    
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
