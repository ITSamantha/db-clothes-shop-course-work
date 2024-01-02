from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from shop.forms import DemandForm


class ContactView(FormView):
    template_name = 'shop/contact.html'
    form_class = DemandForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your demand has been successfully sent!')
        return self.render_to_response(self.get_context_data(form=DemandForm()))

    def form_invalid(self, form):
        messages.error(self.request, 'Something went wrong!')
        return self.render_to_response(self.get_context_data(form=form))


class TopicView(TemplateView):
    template_name = 'shop/topics.html'

    def get_context_data(self, **kwargs):
        title = kwargs['topic']
        context = super().get_context_data(**kwargs)
        context['title'] = title
        context['is_invisible'] = True
        return context


# Error views
def page_not_found(request, exception):
    return render(request, 'shop/errors/error404.html')


def server_error(request, exception):
    return render(request, 'shop/errors/error500.html')
