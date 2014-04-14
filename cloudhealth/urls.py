from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'cloudhealth.views.home', name='home'),
    # url(r'^cloudhealth/', include('cloudhealth.foo.urls')),
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^home$', TemplateView.as_view(template_name="home.html"), name="home"),
    url(r'^profile', include('profile.urls')),
    url(r'^messages', include('message.urls')),
    url(r'^dashboard', include('dashboard.urls')),
    url(r'^about$', TemplateView.as_view(template_name="about.html"), name="about"),
    url(r'^aboutdev', TemplateView.as_view(template_name="aboutdev.html"), name="aboutdev"),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('profile.urls', namespace='profile')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    #(r'^accounts/', include('registration.urls')),
)
