'''
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
   и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
   переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния
   (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
   Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
   Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''

from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        print("Let's go")
        duration = [7, 2, 10]
        i = 0
        while i < 3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(duration[0])
            if i == 1:
                sleep(duration[1])
            if i == 2:
                sleep(duration[2])
            i += 1


light = TrafficLight()
light.running()

