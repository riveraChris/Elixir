from __future__ import absolute_import

from celery import shared_task
from django.conf import settings
from twilio.rest import TwilioRestClient

import arrow

from .models import Appointment


# Uses credentials from the TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
# environment variables
client = TwilioRestClient(account='AC8b805ad5b5bc53b4d233ee6461237fb9',
                              token='99e289c4ca4cf1e22df50677e5584e53')
@shared_task
def send_sms_reminder(appointment_id):
    """Send a reminder to a phone using Twilio SMS"""
    # Get our appointment from the database
    try:
        appointment = Appointment.objects.get(pk=appointment_id)
    except Appointment.DoesNotExist:
        # The appointment we were trying to remind someone about
        # has been deleted, so we don't need to do anything
        return

    appointment_time = arrow.get(appointment.time, appointment.time_zone.zone)
    body = 'Hi {0}. You have an appointment coming up at {1}.'.format(
        appointment.name,
        appointment_time.format('h:mm a')
    )

    message = client.messages.create(
        body=body,
        to="+1" + appointment.phone,
        from_ = "+17874930483",
    )