from django.contrib.auth.views import LoginView
from django.urls import reverse


class MyLoginView(LoginView):

    def get_success_url(self):
        return reverse('blog:profile', args=[self.request.user.username])
