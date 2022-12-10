from django.urls import path

from santai.views import main, bali, massages, thai, slim, neck, foot, stone, herbal_bags, oil, contacts, \
    orders, policy, hawaii, santai, love_candle, oil_four_hands

urlpatterns = [
    path("", main),
    path("massages/", massages),
    path("massages/bali/", bali),
    path("massages/thai/", thai),
    path("massages/slim/", slim),
    path("massages/neck/", neck),
    path("massages/foot/", foot),
    path("massages/stone/", stone),
    path("massages/herbal_bags/", herbal_bags),
    path("massages/oil/", oil),
    path("massages/hawaii/", hawaii),
    path("massages/santai/", santai),
    path("massages/love_candle/", love_candle),
    path("massages/oil_four_hands/", oil_four_hands),
    path("contacts/", contacts),
    path("orders/", orders),
    path("policy/", policy),
]
