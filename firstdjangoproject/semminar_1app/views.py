from django.shortcuts import render
from django.http import HttpResponse
from random import random, randint, choice
import logging
from .models import CoinFlip
from .forms import Sem4Task1

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

#Семминар 1 функции для трех маршрутов

# def coin(request, amount_flips): - 1-2 Задача 2 семминара с импользованием модели
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

#Семминар 1-2 функции для трех маршрутов и проброс контекста в шаблон

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



#Семминар 4 Задание 1-2
# Доработаем задачу про броски монеты, игральной кости и случайного числа.
# Создайте форму, которая предлагает выбрать: монета, кости, числа.
# Второе поле предлагает указать количество попыток от 1 до 64.
def result(request):
    func = {"Coin": coin, "Dice": dice, "Hundred": random_number}
    if request.method == 'POST':
        form = Sem4Task1(request.POST)
        if form.is_valid():
            method = form.cleaned_data['method']
            count = form.cleaned_data['count']
            return func[method](request, count)
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = Sem4Task1()
    return render(request, 'semminar_1app/result.html', {'form': form})
