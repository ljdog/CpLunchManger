# encoding: utf-8
from django.conf.urls import patterns, include, url

from django.conf import settings
from website.views import Home, About

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'website.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', include('frontend.urls')),
                       url(r'^about/$', About),


                       # 后台管理
                        url(r'^mg$', Home),
                       url(r'^accounts/', include('mg.urls')),

                       # static
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.STATIC_ROOT,}),
                       )
