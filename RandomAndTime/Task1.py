"""
В быстрых шахматах на принятие решений для всех ходов игроку даётся 30 минут. Программа должна:
Предлагать ввод хода (например, E2–E4) и считать потраченное время.
После получения хода печатать оставшееся время в минутах.
Если 30 минут закончились или игрок вводит «off» — завершать работу.
Оформить в виде функции.
"""
from time import *

def counter():
    while True:
        action = input("Введите Ваш ход: ")
        start = time()
        action = input("Введите Ваш ход: ")
        end = time()
        if action != "off":
            remains = 30*60 - (end - start)
            if remains < 30*60:
                print("Осталось:", remains//60, "мин.")
            else:
                print("Время закончиллось.")
        else:
            break

counter()