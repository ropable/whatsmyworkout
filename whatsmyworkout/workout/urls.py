from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.LandingPage.as_view(), name='landing_page'),
)
