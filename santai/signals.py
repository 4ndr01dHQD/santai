from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from santai.models import Order, CertificateOrder


@receiver(post_save, sender=Order)
def send_activate_letter_after_save(sender, **kwargs):
    order = kwargs.get('instance')
    send_notification_letter(order.phone, order.name)


@receiver(post_save, sender=CertificateOrder)
def send_activate_letter_after_save(sender, **kwargs):
    certificate_order = kwargs.get('instance')
    send_notification_certificate_letter(certificate_order.phone, certificate_order.name, certificate_order.massage,
                                         certificate_order.time)


def send_notification_letter(phone, name):
    r = send_mail('Уведомление с сайта santai31.ru!',
                  f"Клиент {name} оставил заявку на консультацию, номер обратной связи {phone}.",
                  settings.EMAIL_HOST_USER, ['Santaispa@yandex.ru'])


def send_notification_certificate_letter(phone, name, massage, time):
    r = send_mail('Уведомление с сайта santai31.ru!',
                  f"Клиент {name} оставил заявку на покупку сертификата на массаж {massage} на {time} минут, номер обратной связи {phone}.",
                  settings.EMAIL_HOST_USER, ['Santaispa@yandex.ru'])
