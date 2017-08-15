import pdb
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.core.mail import send_mail
from validate_email import validate_email
from django.conf import settings

# Create your views here.
def index(request):

    page_data = {}
    if request.method == 'POST':
        message = 'Appointment Request' + "\n"
        message += 'Name: ' + request.POST.get('booking_guest_name') + "\n"
        message += 'Phone: ' + request.POST.get('booking_phone') + "\n"
        message += 'Email: ' + request.POST.get('booking_email') + "\n"
        message += 'Date: ' + request.POST.get('booking_arrival_date') + "\n"
        message += 'Time: ' + request.POST.get('booking_time') + "\n"
        message += 'Message: ' + request.POST.get('booking_comments') + "\n\n"
        message += settings.EMAIL_SIGNATURE
        send_mail(settings.EMAIL_APPOINTMENT_SUBJECT, message,  settings.EMAIL_TO, [settings.EMAIL_TO], fail_silently=False)
        return JsonResponse({})

    page_data.update(csrf(request))
    return render_to_response('home.html', page_data)

def sendmessage(request):

    if request.method == 'POST':
        message = 'Message Details' + "\n"
        message += 'Name: ' + request.POST.get('form_name') + "\n"
        message += 'Phone: ' + request.POST.get('form_phone') + "\n"
        message += 'Email: ' + request.POST.get('form_email') + "\n"
        message += 'Message: ' + request.POST.get('form_message') + "\n\n"
        message += settings.EMAIL_SIGNATURE
        send_mail(settings.EMAIL_CONTACTUS_SUBJECT, message, settings.EMAIL_TO, [settings.EMAIL_TO], fail_silently=False)
    return JsonResponse({})

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
