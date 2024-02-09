from datetime import datetime, timedelta
import pytz
from django.core.cache import cache
from django.conf import settings
from main.models import Mailing, Logs
from users.services import send_sms, send_mail_user


def my_job():
    day = timedelta(days=1)
    weak = timedelta(days=7)
    month = timedelta(days=28)

    mailings = Mailing.objects.all().filter(is_activated=True)

    today = datetime.now(pytz.timezone('Europe/Moscow'))
    mailings = mailings.filter(next_date__lte=today)

    for mailing in mailings:
        if mailing.status != 'Завершена':
            mailing.status = 'Запущена'
            mailing.save()
            emails_list = [client.email for client in mailing.mail_to.all()]

            result = send_mail_user(
                subject=mailing.message.subject,
                message=mailing.message.body,
                email_list=emails_list,
            )

            status = result == 1

            log = Logs(mailing=mailing, status=status)
            log.save()

            if status:
                if mailing.next_date < mailing.end_date:
                    mailing.status = 'Создана'
                else:
                    mailing.status = 'Завершена'

            if mailing.periodicity == 'Раз в день':
                mailing.next_date = log.last_mailing_time + day
            elif mailing.periodicity == 'Раз в неделю':
                mailing.next_date = log.last_mailing_time + weak
            elif mailing.periodicity == 'Раз в месяц':
                mailing.next_date = log.last_mailing_time + month

            mailing.save()
            print(f'Рассылка {mailing.name} отправлена')


def get_cache_mailing_count():
    if settings.CACHE_ENABLED:
        key = 'mailings_count'
        mailings_count = cache.get(key)
        if mailings_count is None:
            mailings_count = Mailing.objects.all().count()
            cache.set(key, mailings_count)
    else:
        mailings_count = Mailing.objects.all().count()
    return mailings_count


def get_cache_mailing_active():
    if settings.CACHE_ENABLED:
        key = 'active_mailings_count'
        active_mailings_count = cache.get(key)
        if active_mailings_count is None:
            active_mailings_count = Mailing.objects.filter(is_activated=True).count()
            cache.set(key, active_mailings_count)
    else:
        active_mailings_count = Mailing.objects.filter(is_activated=True).count()
    return active_mailings_count
