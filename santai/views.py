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
            '60': '2400',
            '90': '3400',
            '120': '4400',
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
            '60': '3400',
            '90': '4400',
        }
    },
    {
        'title': 'Массаж шейно-воротниковой зоны + спина',
        'url': 'neck',
        'img': 'facial-treatment',
        'prices': {
            '60': '1400',
            '90': '2400',
        }
    },
    {
        'title': 'Foot массаж',
        'url': 'foot',
        'img': 'foot',
        'prices': {
            '60': '1400',
            '90': '2400',
        }
    },
    {
        'title': 'Стоун массаж',
        'url': 'stone',
        'img': 'stone',
        'prices': {
            '60': '3200',
            '90': '4200',
            '120': '5200',
        }
    },
    {
        'title': 'Массаж травянными мешочками',
        'url': 'herbal_bags',
        'img': 'herbal_bags',
        'prices': {
            '60': '3200',
            '90': '4200',
            '120': '5200',
        }
    },
    {
        'title': 'Арома-ойл массаж',
        'url': 'oil',
        'img': 'oil',
        'prices': {
            '60': '4700',
            '90': '5700',
            '120': '6700',
        }
    },
    {
        'title': 'Гавайский массаж Ломи-Ломи',
        'url': 'hawaii',
        'img': 'hawaii',
        'prices': {
            '60': '3200',
            '90': '4200',
            '120': '5200',
        }
    },
    {
        'title': 'SANTAI массаж',
        'url': 'santai',
        'img': 'santai',
        'prices': {
            '60': '3400',
            '90': '4400',
            '120': '5400',
        }
    },
    {
        'title': 'Свеча любви',
        'url': 'love_candle',
        'img': 'love_candle',
        'prices': {
            '60': '3200',
            '90': '4200',
            '120': '5200',
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
            '60': '3200',
            '90': '4200',
            '120': '5200',
        }
    },
    {
        'title': 'Креольский Bamboo массаж',
        'url': 'bamboo',
        'img': 'bamboo',
        'prices': {
            '60': '3200',
            '90': '4200',
            '120': '5200',
        }
    },
]


def main(request):
    massages = [
        {
            'title': 'Тайский массаж',
            'url': 'thai',
            'img': 'buddha',
            'price': '2400'
        },
        {
            'title': 'Балийский массаж',
            'url': 'bali',
            'img': 'flower',
            'price': '3200'
        },
        {
            'title': 'Гавайский массаж Ломи-Ломи',
            'url': 'hawaii',
            'img': 'hawaii',
            'price': '3200'
        },
        {
            'title': 'Slim массаж',
            'url': 'slim',
            'img': 'massage',
            'price': '3400'
        },
        {
            'title': 'Массаж шейно-воротниковой зоны + спина',
            'url': 'neck',
            'img': 'facial-treatment',
            'price': '1400'
        },
        {
            'title': 'Foot массаж',
            'url': 'foot',
            'img': 'foot',
            'price': '1400'
        },
        {
            'title': 'SANTAI массаж',
            'url': 'santai',
            'img': 'santai',
            'price': '3400'
        },
        {
            'title': 'Свеча любви',
            'url': 'love_candle',
            'img': 'love_candle',
            'price': '3200'
        },
    ]
    return render(request, 'main.html', context={'massages': massages})


def thai(request):
    return render(request, 'massages/thai.html')


def bali(request):
    return render(request, 'massages/bali.html')


def slim(request):
    return render(request, 'massages/slim.html')


def neck(request):
    return render(request, 'massages/neck.html')


def foot(request):
    return render(request, 'massages/foot.html')


def stone(request):
    return render(request, 'massages/stone.html')


def herbal(request):
    return render(request, 'massages/herbal.html')


def herbal_bags(request):
    return render(request, 'massages/herbal_bags.html')


def oil(request):
    return render(request, 'massages/oil.html')


def contacts(request):
    return render(request, 'contacts.html')


def policy(request):
    return render(request, 'policy.html')


def hawaii(request):
    return render(request, 'massages/hawaii.html')


def santai(request):
    return render(request, 'massages/santai.html')


def love_candle(request):
    return render(request, 'massages/love_candle.html')


def oil_four_hands(request):
    return render(request, 'massages/oil_four_hands.html')


def shiatsu(request):
    return render(request, 'massages/shiatsu.html')


def bamboo(request):
    return render(request, 'massages/bamboo.html')


def certificate(request):
    return render(request, 'certificate.html', context={'massages': MASSAGES})


def massages(request):
    return render(request, 'massages.html', context={'massages': MASSAGES})


def promotions(request):
    return render(request, 'promotions.html')


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
