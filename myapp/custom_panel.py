# myapp/custom_panel.py

from debug_toolbar.panels import Panel
from django.utils.translation import gettext_lazy as _

class CustomPanel(Panel):
    """
    A custom panel to display user-friendly information.
    """
    title = _("User Information")
    template = "custom_panel.html"

    def generate_stats(self, request, response):
        user_info = {
            'is_authenticated': request.user.is_authenticated,
            'username': request.user.username if request.user.is_authenticated else 'Guest',
            'email': request.user.email if request.user.is_authenticated else 'N/A',
        }
        self.record_stats({
            'message': "This is a user-friendly message.",
            'user_info': user_info
        })
