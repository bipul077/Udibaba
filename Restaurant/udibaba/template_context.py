from .models import OrderItem,User
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.shortcuts import render
def get_filters(request):
    print("wowowhahaha")
    op = OrderItem.objects.filter(user=request.user).order_by('-order')
    context = {}
    for o in op:
        if(o.order.status=="delivered"):
            print("bipijan")
            print(o.order.tracking_number)
            abc = o.order.tracking_number
            templatepath = 'order/ordermail.html'
            opc = OrderItem.objects.filter(order=abc)
            print("udiba"+str(opc))
            totamnt = 0
            for a in opc:
                totamnt = a.order.total_price
            useremail = User.objects.filter(username=request.user)
            for b in useremail:
                uemail = b.email
                print("useremail"+uemail)
            context={'ordersed':op,'totsed':totamnt}
            template = get_template(templatepath)
            html = template.render(context)
            email_subject = "Your Order has been Delivered by BIPUL"
            email_body = html
            emails = EmailMessage(
                email_subject,
                email_body,
                'noreply@semycolon.com',
            [uemail],
            )
            emails.content_subtype = 'html'
            emails.send(fail_silently=False)
    return context
    # return render(request, templatepath,context)