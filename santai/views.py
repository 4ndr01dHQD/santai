from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from santai.models import Order, CertificateOrder
from santai.serializers import OrderSerializer, CertificateOrderSerializer

MASSAGES = [
    {
        'title': 'Тайский массаж',
        'url': 'thai',
        'img': 'buddha',
        'prices': {
            '60': '2600',
            '90': '3600',
            '120': '4600',
        }
    },
    {
        'title': 'Балийский массаж',
        'url': 'bali',
        'img': 'flower',
        'prices': {
            '60': '3200',
            '90': '4200',
            '120': '5200',
        }
    },
    {
        'title': 'Slim массаж',
        'url': 'slim',
        'img': 'massage',
        'prices': {
            '60': '3600',
            '90': '4600',
            '120': '5600',
        }
    },
    {
        'title': 'Массаж шейно-воротниковой зоны + спина',
        'url': 'neck',
        'img': 'facial-treatment',
        'prices': {
            '60': '1500',
            '90': '2500',
        }
    },
    {
        'title': 'Foot массаж',
        'url': 'foot',
        'img': 'foot',
        'prices': {
            '60': '1500',
            '90': '2500',
        }
    },
    {
        'title': 'Стоун массаж',
        'url': 'stone',
        'img': 'stone',
        'prices': {
            '60': '3400',
            '90': '4400',
            '120': '5400',
        }
    },
    {
        'title': 'Массаж травянными мешочками',
        'url': 'herbal_bags',
        'img': 'herbal_bags',
        'prices': {
            '60': '3400',
            '90': '4400',
            '120': '5400',
        }
    },
    {
        'title': 'Тайский оил массаж',
        'url': 'oil',
        'img': 'oil',
        'prices': {
            '60': '3400',
            '90': '4400',
            '120': '5400',
        }
    },
    {
        'title': 'Гавайский массаж Ломи-Ломи',
        'url': 'hawaii',
        'img': 'hawaii',
        'prices': {
            '60': '3400',
            '90': '4400',
            '120': '5400',
        }
    },
    {
        'title': 'SANTAI массаж',
        'url': 'santai',
        'img': 'santai',
        'prices': {
            '60': '3600',
            '90': '4600',
            '120': '5600',
        }
    },
    {
        'title': 'Свеча любви',
        'url': 'love_candle',
        'img': 'love_candle',
        'prices': {
            '60': '3600',
            '90': '4600',
            '120': '5600',
        }
    },
    {
        'title': 'Oil-массаж в 4 руки',
        'url': 'oil_four_hands',
        'img': 'oil',
        'prices': {
            '60': '4700',
            '90': '5700',
            '120': '6700',
        }
    },
    {
        'title': 'Шиатцу',
        'url': 'shiatsu',
        'img': 'shiatsu',
        'prices': {
            '60': '3400',
            '90': '4400',
            '120': '5400',
        }
    },
    {
        'title': 'Креольский Bamboo массаж',
        'url': 'bamboo',
        'img': 'bamboo',
        'prices': {
            '60': '3400',
            '90': '4400',
            '120': '5400',
        }
    },
    {
        'title': 'Массаж спины, головы и шеи',
        'url': 'back',
        'img': 'massage',
        'prices': {
            '30': '2600',
            '60': '3600',
        }
    },
    {
        'title': 'Массаж рук и предплечий',
        'url': 'hand_and_shoulders',
        'img': 'hand_and_shoulders',
        'prices': {
            '30': '1500',
            '60': '2500',
        }
    },
    {
        'title': 'Энергетический массаж головы',
        'url': 'head',
        'img': 'facial-treatment',
        'prices': {
            '30': '1500',
            '60': '2500',
        }
    },
]

CAROUSEL_MASSAGE = [
    {
        'title': 'Тайский массаж',
        'url': 'thai',
        'img': 'buddha',
        'price': '2600'
    },
    {
        'title': 'Балийский массаж',
        'url': 'bali',
        'img': 'flower',
        'price': '3400'
    },
    {
        'title': 'Гавайский массаж Ломи-Ломи',
        'url': 'hawaii',
        'img': 'hawaii',
        'price': '3400'
    },
    {
        'title': 'Slim массаж',
        'url': 'slim',
        'img': 'massage',
        'price': '3600'
    },
    {
        'title': 'Массаж шейно-воротниковой зоны + спина',
        'url': 'neck',
        'img': 'facial-treatment',
        'price': '1500'
    },
    {
        'title': 'Foot массаж',
        'url': 'foot',
        'img': 'foot',
        'price': '1500'
    },
    {
        'title': 'SANTAI массаж',
        'url': 'santai',
        'img': 'santai',
        'price': '3600'
    },
    {
        'title': 'Свеча любви',
        'url': 'love_candle',
        'img': 'love_candle',
        'price': '3600'
    },
]


def main(request):
    return render(request, 'main.html', context={'massages': CAROUSEL_MASSAGE})


def thai(request):
    return render(request, 'massages/thai.html', context={"massages": CAROUSEL_MASSAGE})


def bali(request):
    return render(request, 'massages/bali.html', context={"massages": CAROUSEL_MASSAGE})


def slim(request):
    return render(request, 'massages/slim.html', context={"massages": CAROUSEL_MASSAGE})


def neck(request):
    return render(request, 'massages/neck.html', context={"massages": CAROUSEL_MASSAGE})


def foot(request):
    return render(request, 'massages/foot.html', context={"massages": CAROUSEL_MASSAGE})


def stone(request):
    return render(request, 'massages/stone.html', context={"massages": CAROUSEL_MASSAGE})


def herbal(request):
    return render(request, 'massages/herbal.html', context={"massages": CAROUSEL_MASSAGE})


def herbal_bags(request):
    return render(request, 'massages/herbal_bags.html', context={"massages": CAROUSEL_MASSAGE})


def oil(request):
    return render(request, 'massages/oil.html', context={"massages": CAROUSEL_MASSAGE})


def contacts(request):
    return render(request, 'contacts.html')


def policy(request):
    return render(request, 'policy.html')


def hawaii(request):
    return render(request, 'massages/hawaii.html', context={"massages": CAROUSEL_MASSAGE})


def santai(request):
    return render(request, 'massages/santai.html', context={"massages": CAROUSEL_MASSAGE})


def love_candle(request):
    return render(request, 'massages/love_candle.html', context={"massages": CAROUSEL_MASSAGE})


def oil_four_hands(request):
    return render(request, 'massages/oil_four_hands.html', context={"massages": CAROUSEL_MASSAGE})


def shiatsu(request):
    return render(request, 'massages/shiatsu.html', context={"massages": CAROUSEL_MASSAGE})


def bamboo(request):
    return render(request, 'massages/bamboo.html', context={"massages": CAROUSEL_MASSAGE})


def certificate(request):
    return render(request, 'certificate.html', context={'massages': MASSAGES})


def massages(request):
    return render(request, 'massages.html', context={'massages': MASSAGES})


def promotions(request):
    return render(request, 'promotions.html')


def spa(request):
    return render(request, 'spa.html')


def back(request):
    return render(request, 'massages/back.html', context={'massages': CAROUSEL_MASSAGE})


def hand_and_shoulders(request):
    return render(request, 'massages/hand_and_shoulders.html', context={'massages': CAROUSEL_MASSAGE})


def head(request):
    return render(request, 'massages/head.html', context={'massages': CAROUSEL_MASSAGE})


@api_view(['POST'])
def orders(request):
    serializer = OrderSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    order = Order.objects.filter(phone=serializer.validated_data['phone']).first()
    today = timezone.now()
    # todo Добавить сохранение куки, для того, что бы не долбить бэк
    # todo Добавить рекапчу фоновую
    if order:
        if (order.updated_at + timezone.timedelta(days=1)) > today:
            return Response('Заявку можно отправлять не более раза в сутки.', status=status.HTTP_403_FORBIDDEN)
        order.is_permitted = False
        order.name = serializer.validated_data['name']
        order.save()
    else:
        serializer.save()
    return Response('Ваш запрос успешно передан, ожидайте звонка', status=status.HTTP_201_CREATED)


@api_view(['POST'])
def create_certificate(request):
    serializer = CertificateOrderSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    order = CertificateOrder.objects.filter(phone=serializer.validated_data['phone']).first()
    today = timezone.now()
    # # todo Добавить сохранение куки, для того, что бы не долбить бэк
    # # todo Добавить рекапчу фоновую
    if order:
        if (order.created_at + timezone.timedelta(days=1)) > today:
            return Response('Вы ранее уже создавали заявку.', status=status.HTTP_403_FORBIDDEN)
    serializer.save()

    return Response('Заявка создана, ожидайте звонка', status=status.HTTP_201_CREATED)
