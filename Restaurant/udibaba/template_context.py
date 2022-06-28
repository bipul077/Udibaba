from .models import AdHeader, Deliverycharge, Multipleadimage
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.shortcuts import render
def allfunc(request):#this will go to all the page
    dc = Deliverycharge.objects.get(title='KTM')
    dca = dc.Deliverycost
    adhead = AdHeader.objects.all()
    adimg = Multipleadimage.objects.all()
    context = {'shippingcost':dca,'adhead':adhead,'adimg':adimg}
    return context
