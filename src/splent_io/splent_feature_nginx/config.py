"""
Nginx reverse proxy configuration.

Exposes proxy-related settings so hooks and other features
can reference the configured ports and server name.
"""

import os


def inject_config(app):
    app.config.update(
        {
            "NGINX_HTTP_HOST_PORT": os.getenv("NGINX_HTTP_HOST_PORT", "80"),
            "NGINX_HTTPS_HOST_PORT": os.getenv("NGINX_HTTPS_HOST_PORT", "443"),
            "NGINX_SERVER_NAME": os.getenv("NGINX_SERVER_NAME", "localhost"),
        }
    )
