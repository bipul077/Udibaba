from .models import Deliverycharge, OrderItem,User
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.shortcuts import render
def allfunc(request):#this will go to all the page
    dc = Deliverycharge.objects.get(title='KTM')
    dca = dc.Deliverycost
    context = {'shippingcost':dca}
    return context
