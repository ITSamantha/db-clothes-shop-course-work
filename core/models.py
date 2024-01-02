from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class LoginRequiredModelMixin(LoginRequiredMixin):

    def get_success_url(self):
        if hasattr(self, 'success_url'):
            return reverse_lazy(self.success_url)

