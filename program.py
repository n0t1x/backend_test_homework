from datetime import datetime as dt

FORMAT = '%H:%M:%S' # Запишите формат полученного времени.
WEIGHT = 75    # Вес.
HEIGHT = 175   # Рост.
K_1 = 0.035    # Коэффициент для подсчета калорий.
K_2 = 0.029    # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}  # Словарь для хранения полученных данных.


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    # Если длина пакета отлична от 2
    # или один из элементов пакета имеет пустое значение -
    # функция вернет False, иначе - True.
    if len(data) == 2:
        time, steps = data
        if time != None and steps != None:
            return True
        else:
            return False
    else:
        return False
    

def check_correct_time(time):
    """Проверка корректности параметра времени."""
    # Если словарь для хранения не пустой
    # и значение времени, полученное в аргументе,
    # меньше самого большого ключа в словаре,
    # функция вернет False.
    # Иначе - True 
    times = list (storage_data.keys())

    if len(storage_data) != 0:
        max_key = max(times)
        
        if time > max_key:
            return True
        else:
            return False


def get_step_day(steps):
    """Получить количество пройденных шагов за этот день."""
    # Посчитайте все шаги, записанные в словарь storage_data,
    # прибавьте к ним значение из последнего пакета
    # и верните  эту сумму.
    sum_steps = 0
    if len(storage_data) > 0:
        for step in storage_data.values():
            sum_steps += step
    sum_steps += steps
    return sum_steps


def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""
    # Посчитайте дистанцию в километрах,
    # исходя из количества шагов и длины шага.
    #distance = steps*STEP_M/1000
    return steps*STEP_M/1000


def get_spent_calories(dist, time):
    """Получить значения потраченных калорий."""
    # В уроке «Строки» вы написали формулу расчета калорий.
    # Перенесите её сюда и верните результат расчётов.
    # Для расчётов вам потребуется значение времени; 
    # получите его из объекта current_time;
    # переведите часы и минуты в часы, в значение типа float.
    start_day = dt.strptime('0:00:00', FORMAT)
    hours = round((time-start_day).total_seconds()/3600, +2)
    mean_speed = dist / hours
    minutes = hours * 60
    spent_calories = (K_1*WEIGHT + (mean_speed**2 / HEIGHT) * K_2*WEIGHT) * minutes
    return spent_calories


def get_achievement(dist):
    """Получить поздравления за пройденную дистанцию."""
    # В уроке «Строки» вы описали логику
    # вывода сообщений о достижении в зависимости
    # от пройденной дистанции.
    # Перенесите этот код сюда и замените print() на return.
    if dist >= 6.5:
        message = 'Отличный результат! Цель достигнута.'
        return message
    elif dist >= 3.9:
        message = 'Неплохо! День был продуктивным.'
        return message
    elif dist >= 2:
        message = 'Маловато, но завтра наверстаем!'
        return message
    else:
        message = 'Лежать тоже полезно. Главное — участие, а не победа!'
        return message


def show_message (time, day_steps, dist, spent_calories, achievement):
    return f'''
Время: {time.time()}.
Количество шагов за сегодня: {day_steps}.
Дистанция составила {dist:.2f} км.
Вы сожгли {spent_calories:.2f} ккал.
{achievement}
'''


def accept_package(data):
    """Обработать пакет данных."""

    if  check_correct_data(data) == False: # Если функция проверки пакета вернет False
        return f'Некорректный пакет'

    time, steps = data # Распакуйте полученные данные.
    pack_time = (dt.strptime(time, FORMAT)) # Преобразуйте строку с временеи в объект типа time.
    if  check_correct_time(pack_time) == False: # Если функция проверки значения времени вернет False
        return f'Некорректное значение времени'

    day_steps = get_step_day(steps) # Запишите результат подсчёта пройденных шагов.
    dist =  get_distance(day_steps) # Запишите результат расчёта пройденной дистанции.
    spent_calories = get_spent_calories(dist, pack_time) # Запишите результат расчёта сожжённых калорий.
    achievement = get_achievement(dist) # Запишите выбранное мотивирующее сообщение.
    print(show_message(pack_time, day_steps, dist, spent_calories, achievement)) # Вызовите функцию show_message().
    storage_data [pack_time] = day_steps # Добавьте новый элемент в словарь storage_data.
    return storage_data # Верните словарь storage_data.


# Данные для самопроверки.Не удаляйте их.
package_0 = ('2:00:01', 505)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)