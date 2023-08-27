import os
from datetime import datetime
import pytz
import smtplib
from django.conf import settings
from django.core.mail import send_mail

from service.models import Message, Log, Client


def send_email(ms, cl, ml, tz):
    try:
        send_mail(ms.theme, ms.body, settings.EMAIL_HOST_USER, [cl.email])
        log = Log.objects.create(user=cl, mail=ms, last_try_date=datetime.now(tz), server_response='Успешно',
                                 try_status='200')
        log.save()
    except smtplib.SMTPException as err:
        log = Log.objects.create(user=cl, mail=ms, last_try_date=datetime.now(tz), server_response='Ошибка',
                                 try_status=err)
        log.save()


def test_job(aaa=None):
    mails = Message.objects.filter(mailing_status='s')
    tz = pytz.timezone('Europe/Moscow')
    now = datetime.now(tz)
    for mail in mails:
        for client in mail.clients.all():
            ml = Log.objects.filter(user=client, mail=mail)
            print(ml)
            if ml.exists():
                last_mail = ml.order_by('last_try_date').first()
                diff = (now - last_mail.last_try_date).days
                print(diff)
                if mail.periodicity == "d" and diff >= 1:
                    print('test_2')
                    send_email(mail, client, ml, tz)
                if mail.periodicity == "w" and diff >= 7:
                    print('test_3')
                    send_email(mail, client, ml, tz)
                if mail.periodicity == "m" and diff >= 30:
                    print('test_4')
                    send_email(mail, client, ml, tz)
            else:
                send_email(mail, client, ml, tz)
        mail.status = 'f'
        mail.save()
