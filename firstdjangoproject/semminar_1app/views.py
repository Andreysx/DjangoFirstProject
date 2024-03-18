from django.shortcuts import render
from django.http import HttpResponse
from random import random, randint, choice
import logging
from .models import CoinFlip

# Задание №5
# � Создайте новое приложение. Подключите его к проекту. В
# приложении должно быть три простых представления,
# возвращающих HTTP ответ:
# � Орёл или решка
# � Значение одной из шести граней игрального кубика
# � Случайное число от 0 до 100
# � Пропишите маршруты

logger = logging.getLogger(__name__)


def index(request):
    logger.info("Start page")
    return HttpResponse("Hello, world!")



# def coin(request, amount_flips):
#     result = choice(('Head', 'Tails'))
#     logger.info(result)
#     CoinFlip(side=result).save()
#     last_results = CoinFlip.get_last_flips(amount_flips)
#     context = {
#         'current_flip': result,
#         'last_results': last_results
#         }
#     return render(request, 'coin/coin.html', context)
#
# def dice(request):
#     logger.info("Use dice funct")
#     count = randint(1, 6)
#     logger.debug(count)
#     return HttpResponse(f"Значение одной из шести граней игрального кубика = {count}")
#
#
# def random_number(request):
#     logger.info("Use random_number funct")
#     number = randint(1, 100)
#     logger.debug(number)
#     return HttpResponse(f"Случайное число от 0 до 100 = {number}")


def coin(request, amount_flips):
    # logger.info(result)
    #
    results = [choice(('Head', 'Tails')) for _ in range(amount_flips)]
    context = {
        'title': 'Монетка',
        'results': results
        }
    return render(request, 'semminar_1app/result.html', context)


def dice(request, amount_flips):
    results = [randint(1, 6) for _ in range(amount_flips)]

    # logger.debug(count)
    context = {'title': 'Кости', 'results': results}
    return render(request, 'semminar_1app/result.html', context)


def random_number(request, amount_gens):
    results = [randint(1, 100) for _ in range(amount_gens)]
    # logger.debug(count)
    context = {'title': 'Волшебная сотня', 'results': results}
    return render(request, 'semminar_1app/result.html', context)