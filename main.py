import vk_captchasolver as vc # Импорт библиотеки

captcha = vc.solve(image='captcha2.png') # Получаем решение каптчи от картинки
print(captcha) # Выводим в консоль решенную каптчу.

# import vk_captchasolver as vc # Импорт библиотеки
# captcha = vc.solve(sid=74838345480543, s=1) # Решить с помощью параметров sid и s
# captcha = vc.solve(sid=74838345480543) # Решить только с помощью параметра sid
# print(captcha) # Выводим в консоль результат.

import vk_api # Импортируем библиотеку от ВК
import vk_captchasolver as vc # Наша решалка каптчи

# Метод парсит из ссылки(aka URL) параметры от GET запроса.
def get_param_from_url(url, param_name):
    return [i.split("=")[-1] for i in url.split("?", 1)[-1].split("&") if i.startswith(param_name + "=")][0]

def captcha_handler(captcha):
    sid = get_param_from_url(captcha.get_url(), "sid") # Парсим параметр sid из ссылки
    s = get_param_from_url(captcha.get_url(), "s") # Парсим параметр s из ссылки
    return captcha.try_again(vc.solve(sid=int(sid), s=int(s))) # Просим вк попробовать еще раз вместе с решенной каптчей

vk_session = vk_api.VkApi(token = "токенвк", captcha_handler=captcha_handler) # Создание сессии ВК с captcha_handler
vk = vk_session.get_api() # Получаем API от сессии