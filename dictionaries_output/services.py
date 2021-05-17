from dictionaries_output.models import *


# import openpyxl


def get_context_model(request, dictionary_name):
    model_content = None
    if dictionary_name == 'Productions':
        model_content = Productions.objects.all()
    elif dictionary_name == 'Workshops':
        model_content = Workshops.objects.all()
    elif dictionary_name == 'Compartments':
        model_content = Compartments.objects.all()
    elif dictionary_name == 'SwitchCabinets':
        model_content = SwitchCabinets.objects.all()
    elif dictionary_name == 'Stations':
        model_content = Stations.objects.all()
    return model_content


#
# Entry.objects.filter(headline__startswith='What').exclude(pub_date__gte=datetime.date.today()).filter(
#     pub_date__gte=datetime(2005, 1, 30))


def get_hierarchy_context_model(request, dictionary_name, model_content_pk, ):
    model_content = Locations.objects.filter(production_id=model_content_pk)
    if dictionary_name == 'Productions':
        model_content = Locations.objects.filter(production_id=model_content_pk)
    elif dictionary_name == 'Workshops':
        model_content = Locations.objects.filter(workshop_id=model_content_pk)
    elif dictionary_name == 'Compartments':
        model_content = Locations.objects.filter(compartment_id=model_content_pk)
    elif dictionary_name == 'SwitchCabinets':
        model_content = Locations.objects.filter(location_id=model_content_pk)
    elif dictionary_name == 'Stations':
        model_content = Locations.objects.filter(location_id=model_content_pk)
    # for item in model_content:
    #     a= item
    # print(model_content)
    return model_content
