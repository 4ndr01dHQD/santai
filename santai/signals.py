from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from santai.models import Order


@receiver(post_save, sender=Order)
def send_activate_letter_after_save(sender, **kwargs):
    order = kwargs.get('instance')
    send_notification_letter(order.phone, order.name)


def send_notification_letter(phone, name):
    r = send_mail('Уведомление с сайта santai31.ru!',
                  f"Клиент {name} оставил заявку на консультацию, номер обратной связи {phone}.",
                  settings.EMAIL_HOST_USER, ['Santaispa@yandex.ru'])
