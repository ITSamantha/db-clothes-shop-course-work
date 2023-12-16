from django.shortcuts import render
from django.views.generic import TemplateView

import dictionaries.topics
from products.models import Category


# Create your views here.

def cart(request):
    categories = Category.objects.all()
    context = {
        # 'features': FEATURES,
        'topics': dictionaries.topics.TOPICS,
        # 'networks': dictionaries.networks.NETWORKS,
        'categories': categories,
    }
    return render(request, 'orders/cart.html', context=context)


class CheckoutView(TemplateView):
    template_name = 'orders/checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class FavouritesView(TemplateView):
    template_name = 'orders/favourites.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def add_to_cart(request, product):
    pass
