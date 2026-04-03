from splent_framework.hooks.template_hooks import register_template_hook
from flask import current_app


def nginx_sidebar_link():
    port = current_app.config.get("NGINX_HTTP_HOST_PORT", "80")
    return (
        '<li class="sidebar-item">'
        f'<a class="sidebar-link" href="http://localhost:{port}" target="_blank">'
        '<i class="align-middle" data-feather="globe"></i> '
        '<span class="align-middle">Nginx</span>'
        "</a>"
        "</li>"
    )


register_template_hook("layout.authenticated_sidebar", nginx_sidebar_link)
