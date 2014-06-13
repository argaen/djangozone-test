from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'posts.views.list', name='posts_list'),
    url(r'^about/$', 'common.views.about', name='about'),

    url(r'^admin/', include(admin.site.urls)),
)
