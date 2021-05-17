from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from dictionaries_output.services import *
from django.shortcuts import render


# from django.views.generic import ListView

# Подумать над классами представлениями
# class DictionariesOutputBaseView(ListView):
#
#     template_name = 'base_dict_output.html'
#     def get_context_data(self, *, object_list=None, **kwargs):
#         pass


def rendering_dict(request, dictionary_name):
    model_context = get_context_model(request, dictionary_name)
    context = {
        'model_context': model_context,
        'title': 'жопа',
        'path': dictionary_name,
    }
    return render(request, template_name='index.html', context=context)


def rendering_hierarchy_dependent_dict(request, dictionary_name, model_content_pk):
    model_context = get_hierarchy_context_model(request, dictionary_name, model_content_pk)
    context = {
        'model_context': model_context,
        'title': 'жопа',
        'path': model_content_pk,
    }
    return render(request, template_name='index.html', context=context)
