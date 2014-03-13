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
    url(r'^home$', TemplateView.as_view(template_name="home.html")),
    url(r'^profile', TemplateView.as_view(template_name="profile.html")),
    url(r'^message', TemplateView.as_view(template_name="message.html")),
    url(r'^dashboard', TemplateView.as_view(template_name="dashboard.html")),
    url(r'^about', TemplateView.as_view(template_name="about.html")),
    url(r'^aboutdev', TemplateView.as_view(template_name="aboutdev.html")),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^accounts/', include('registration.backends.simple.urls')),
    #(r'^accounts/', include('registration.urls')),
)
