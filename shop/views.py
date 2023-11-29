from django.shortcuts import render

import dictionaries.topics


# Create your views here.


def contact(request):
    return render(request, 'shop/contact.html')


def topic(request, topic):
    context = {
        'title': topic,
        'is_invisible': True,
    }
    return render(request, f'shop/topics/{topic}.html', context=context)
