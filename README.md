**Проект:**\
UI авто тестирование добавления товара из карточки в корзину интернет магазина ***Детский Мир***.   
<https://www.detmir.ru/product/index/id/3192878/>   

**Проект выполнен на Python 3.9**\
Использовались библиотеки ***Pytest*** и ***Selenium***   
Проект выполнен с использованием архитектуры ***PageObject***   
Браузер Google Chrome версия 114.0.5735.199 и chromedriver для этой версии.  
Chromedriver лежит в корневой папке проекта, что позволяет запускать тесты из среды разработки (***PyCharm***)  
используя кнопку пуска ***"Run"***.  
Также все тесты можно запустить разом командой из терминала:  
*python -m pytest -v --driver Chrome*  

Для проверки добавления товара в корзину используем два теста, первый до добавления проверяет наличие
в кнопке добавления товара надписи "В корзину". Второй, после добавления товара в корзину, проверяет отсутствие текста
"В корзину".
Также можно проверить наличие товара в корзине перейдя в корзину и убедившись в наличии там товара.
