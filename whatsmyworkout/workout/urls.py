from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.TemplateView.as_view(template_name='landing.html'), name='landing'),
    url(r'^workout$', views.WorkoutPage.as_view(), name='workout'),
    url(r'^workout\.json$', views.WorkoutJson.as_view(), name='workout_json'),
    url(r'^disclaimer$', TemplateView.as_view(template_name='disclaimer.html'), name='disclaimer'),
)
