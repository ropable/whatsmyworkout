"""
WSGI config for whatsmyworkout project.
It exposes the WSGI callable as a module-level variable named ``application``.
"""
import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "whatsmyworkout.settings.base")
application = Cling(MediaCling(get_wsgi_application()))
