from django.conf import settings
from django.shortcuts import redirect

class AdminSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is accessing the admin dashboard
        if request.path.startswith('/admin/') and not request.session.get(settings.ADMIN_SESSION_KEY):
            return redirect('/custom-admin/login/')
        return self.get_response(request)