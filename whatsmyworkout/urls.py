from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Next line is to remove the logout confirmation step.
    #url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    #url(r'^accounts/', include('allauth.urls')),
    #url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include('workout.urls')),
    url(r'^$', TemplateView.as_view(template_name='landing.html'), name='landing'),
]
