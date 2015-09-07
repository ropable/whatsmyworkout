from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Next line is to remove the logout confirmation step.
    #url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    #url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('workout.urls')),
]
