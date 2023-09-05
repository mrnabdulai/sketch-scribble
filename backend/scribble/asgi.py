"""
ASGI config for scribble project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack

# from channels.security.websocket import AllowedHostsOriginValidator
import scribbleapp.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scribble.settings")

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AuthMiddlewareStack(
            URLRouter(scribbleapp.routing.websocket_urlpatterns)
        ),  # We will add websocket routes later
        # Just HTTP for now. (We can add other protocols later.)
    }
)