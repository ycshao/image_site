from django.conf.urls import patterns, include, url
from image_site.views import hello, home, current_datetime, hours_ahead, display_meta
from image_site.books.views import search
from image_site.contact.views import contact

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^meta/$', display_meta),
    url(r'^search/$', search),
    url(r'^contact/$', contact),
    # Examples:
    # url(r'^$', 'image_site.views.home', name='home'),
    # url(r'^image_site/', include('image_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
