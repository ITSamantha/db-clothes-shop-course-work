from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView

from users.forms import RegistrationForm, LoginForm, ProfileForm
from shop.forms import SubscribeForm


class LoginUserView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')


class LogoutUserView(LoginRequiredMixin, LogoutView):
    template_name = 'products/index.html'
    success_url = reverse_lazy('users:login')


class RegisterUserView(CreateView):
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    form_class = RegistrationForm

    class Meta:
        model = get_user_model()

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class SubscribeView(FormView):
    template_name = 'shop/includes/subscribe.html'
    form_class = SubscribeForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'You successfully subscribed :)')
        return self.render_to_response(self.get_context_data(form=form))


class ProfileUserView(LoginRequiredMixin, FormView):
    template_name = 'users/profile.html'
    form_class = ProfileForm
    success_url = 'users:profile'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'The new data has been successfully saved!')
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy(self.success_url)

# @login_required
# def profile(request):
#     if request.method == 'GET':
#         form = ProfileForm(instance=request.user)
#     else:
#         form = ProfileForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'users/profile.html', context=context)

# def login_user(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             username = cleaned_data['username']
#             password = cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user and user.is_active:  # Block
#                 login(request, user)
#                 return redirect('index')
#     else:
#         form = LoginForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'users/login.html', context=context)


# def logout_user(request):
#     logout(request)
#     return render(request, 'products/index.html')


# def subscribe(request):
#     if request.method == 'POST':
#         form = SubscribeForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     else:
#         form = SubscribeForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'shop/includes/subscribe.html', context=context)


# def register_user(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('users:login')
#     else:
#         form = RegistrationForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'users/register.html', context=context)
