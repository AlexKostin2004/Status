import vk_api

import datetime # работа с датой и временем

import time

while True:
	vk = vk_api.VkApi(token="532c8e3c64df9dec413346b00602716e0d4ef17763df61642c412cb0a5e15ba7e335f9e35a40c5c2ea310")
	delta = datetime.timedelta(hours=6, minutes=0) # разница от UTC. Можете вписать любое значение вместо 3
	t = (datetime.datetime.now(datetime.timezone.utc) + delta) # Присваиваем дату и время переменной «t»
	nowtime = t.strftime("%H:%M") # текущее время
	nowdate = t.strftime("%d.%m.%Y") # текущая дата
	vk.method("status.set", {"text": nowtime + "  " + nowdate})
	time.sleep(30) # погружаем скрипт в «сон» на 30 секунд
