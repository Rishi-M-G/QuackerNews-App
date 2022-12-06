"""
ASGI config for quacker project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
>>>>>>> 7a59026 (Final Sprint)
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quacker.settings')

application = get_asgi_application()
=======
# delete later
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quacker.settings')
django_asgi_app = get_asgi_application()

import chat.routing
django.setup()

# delete later
application = ProtocolTypeRouter(
    {
        'http': django_asgi_app,
        'websocket': AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(chat.routing.websocket_urlpatterns))
        ),
    }
)
>>>>>>> 7a59026 (Final Sprint)
