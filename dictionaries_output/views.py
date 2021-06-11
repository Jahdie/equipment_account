from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from dictionaries_output.models import *
from django.shortcuts import render
from django.views.generic import ListView, DetailView


# Подумать над классами представлениями
class ProductionsListView(ListView):
    model = Productions
    template_name = 'productions_list.html'
    context_object_name = 'productions'

    # extra_context = {'title': 'Производство'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Производство'
        return context


class WorkshopsListView(ListView):
    model = Workshops
    template_name = 'workshops_list.html'
    context_object_name = 'workshops'
    allow_empty = False
    # extra_context = {'title': 'Производство'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Цеха'
        context['workshops_by_production'] = Workshops.objects.filter(production_id=self.kwargs['production_id'])
        return context
    # def get_queryset(self):
    #     return Productions.objects.filter(name='НОФ')


class CompartmentsListView(ListView):
    model = Compartments
    template_name = 'compartments_list.html'
    context_object_name = 'compartments'

    # extra_context = {'title': 'Производство'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Цех'
        context['compartments_by_workshop'] = Compartments.objects.filter(workshop_id=self.kwargs['workshop_id'])
        return context
    # def get_queryset(self):
    #     return Productions.objects.filter(name='НОФ')


class LocationsListView(ListView):
    model = Locations
    context_object_name = 'locations'

    # extra_context = {'title': 'Производство'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Местоположение'
        return context
    # def get_queryset(self):
    #     return Productions.objects.filter(name='НОФ')


class StationsListView(ListView):
    model = Stations
    template_name = 'stations_list.html'
    context_object_name = 'stations'

    # extra_context = {'title': 'Производство'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Цех'
        context['stations_by_compartment'] = Stations.objects.filter(compartment_id=self.kwargs['compartment_id'])
        return context
    # def get_queryset(self):
    #     return Productions.objects.filter(name='НОФ')

# def rendering_dict(request, dictionary_name):
#     model_context = get_context_model(request, dictionary_name)
#     context = {
#         'model_context': model_context,
#         'title': 'жопа',
#         'path': dictionary_name,
#     }
#     return render(request, template_name='index.html', context=context)
#
#
# def rendering_hierarchy_dependent_dict(request, dictionary_name, model_content_pk):
#     model_context = get_hierarchy_context_model(request, dictionary_name, model_content_pk)
#     context = {
#         'model_context': model_context,
#         'title': 'жопа',
#         'path': model_content_pk,
#     }
#     return render(request, template_name='index.html', context=context)
