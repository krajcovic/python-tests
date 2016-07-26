import logging

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views import generic

from wifimonitor.models import Device

# Get an instance of a logger
logger = logging.getLogger(__name__)


class IndexView(generic.ListView):
    template_name = 'wifi/index.html'
    context_object_name = 'connected_list'

    def get_queryset(self):
        """Return the last five published questions."""
        # return Device.objects.order_by('-pub_date')[:5]
        return Device.objects.all()