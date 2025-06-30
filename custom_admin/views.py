from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.models import User

class CustomAdminLoginView(LoginView):
    template_name = 'custom_admin/login.html'

    def form_valid(self, form):
        # Check if the user has admin privileges
        user = form.get_user()
        if not user.is_staff:  # Only allow staff/admin users to log in
            form.add_error(None, "You do not have permission to access the admin panel.")
            return self.form_invalid(form)

        # Log in the admin user
        login(self.request, user)

        # Set a custom session key for admin
        self.request.session[settings.ADMIN_SESSION_KEY] = True

        # Redirect to the admin dashboard
        return redirect('/admin/')

    def form_invalid(self, form):
        # Render the login page with an error message
        return self.render_to_response(self.get_context_data(form=form))

custom_admin_login = CustomAdminLoginView.as_view()
