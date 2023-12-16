from django.shortcuts import render
from django.views.generic import TemplateView

import dictionaries.topics


# Create your views here.

class ContactView(TemplateView):
    template_name = 'shop/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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
