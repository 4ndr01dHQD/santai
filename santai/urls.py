from django.urls import path

from santai.views import main, bali, massages, thai, lymphatic_drainage, neck, foot, stone, herbal_bags, oil, contacts, \
    orders

urlpatterns = [
    path("", main),
    path("massages/", massages),
    path("massages/bali/", bali),
    path("massages/thai/", thai),
    path("massages/lymphatic_drainage/", lymphatic_drainage),
    path("massages/neck/", neck),
    path("massages/foot/", foot),
    path("massages/stone/", stone),
    path("massages/herbal_bags/", herbal_bags),
    path("massages/oil/", oil),
    path("contacts/", contacts),
    path("orders/", orders),
]
