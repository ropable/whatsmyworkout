from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.LandingPage.as_view(), name='landing_page'),
    url(r'^workout$', views.WorkoutPage.as_view(), name='workout_page'),
    url(r'^why$', TemplateView.as_view(template_name='workout/why.html'), name='why_bodyweight'),
)
