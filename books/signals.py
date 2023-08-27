from django.shortcuts import get_object_or_404
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from .models import book
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        # payment was successful
        bk = get_object_or_404(book, id=ipn.invoice)

        if bk.price() == ipn.mc_gross:
            # mark the order as paid
             send_mail('hi this is','this is a link you can use to download the item you bought from our site'+bk.file,settings.EMAIL_HOST_USER,[User.email],fail_silently=False)
             User.email_user(User,'hi','this is the item you bought from us'+bk.file,settings.EMAIL_HOST_USER,fail_silently=False)