from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from santai.models import Order
from santai.serializers import OrderSerializer


def main(request):
    massages = [
        {
            'title': 'Тайский массаж',
            'url': 'thai',
            'img': 'buddha',
        },
        {
            'title': 'Балийский массаж',
            'url': 'bali',
            'img': 'flower',
        },
        {
            'title': 'Slim массаж',
            'url': 'lymphatic_drainage',
            'img': 'massage',
        },
        {
            'title': 'Массаж шейно-воротниковой зоны + спина',
            'url': 'neck',
            'img': 'facial-treatment',
        },
        {
            'title': 'Foot массаж',
            'url': 'foot',
            'img': 'foot',
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


def massages(request):
    massages = [
        {
            'title': 'Тайский массаж',
            'url': 'thai',
            'img': 'buddha',
        },
        {
            'title': 'Балийский массаж',
            'url': 'bali',
            'img': 'flower',
        },
        {
            'title': 'Slim массаж',
            'url': 'slim',
            'img': 'massage',
        },
        {
            'title': 'Массаж шейно-воротниковой зоны + спина',
            'url': 'neck',
            'img': 'facial-treatment',
        },
        {
            'title': 'Foot массаж',
            'url': 'foot',
            'img': 'foot',
        },
        {
            'title': 'Стоун массаж',
            'url': 'stone',
            'img': 'stone',
        },
        {
            'title': 'Массаж травянными мешочками',
            'url': 'herbal_bags',
            'img': 'herbal_bags',
        },
        {
            'title': 'Арома-ойл массаж',
            'url': 'oil',
            'img': 'oil',
        },
    ]

    return render(request, 'massages.html', context={'massages': massages})


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
