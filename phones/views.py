from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Phone, PhoneModel, PhoneStorage, PhoneColor
from .forms import PhoneCreateForm

# Create your views here.
# return a list of all phones
class PhoneListView(ListView):
    model = Phone
    template_name = 'phones/phone_list.html'
    context_object_name = 'phones'
    paginate_by = 10
    # sort the phone list by created_at reverse
    queryset = Phone.objects.all().order_by('-created_at')


"""
# Create getstorage view for AJAX call
def getstorage(request):
    # Get the model id
    model_id = request.GET.get('model_id')
    # Get the storage based on the model id
    storages = PhoneStorage.objects.filter(phonemodel_id=model_id).order_by('storage')
    # Return the storage as JSON
    return render(request, 'phones/storage_dropdown_list_options.html', {'storages': storages})
"""

# Create a view for technican to add phone
class PhoneCreateView(View):
    def get(self, request, *args, **kwargs):
        form = PhoneCreateForm()
        context = {
            'form': form
        }
        return render(request, 'phones/phone_create.html', context)

    def post(self, request, *args, **kwargs):
        form = PhoneCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = PhoneCreateForm()
        context = {
            'form': form
        }
        return render(request, 'phones/phone_create.html', context)