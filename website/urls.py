from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^sendmessage/', views.sendmessage, name='sendmessage'),
    url(r'^member-booking-form/', views.bookingform, name='bookingform'),
    url(r'^bootstrap-parent-modal/', views.bootstrapmodal, name='bootstrapmodal'),
]
