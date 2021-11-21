# Gray_filter
Результат работы профилирования filter.py - 17.713 сек.
![alt text](Pic/a1.PNG)
Результат профилирования old_filter.py – 37.509 сек.
![alt text](Pic/a2.PNG)
Несмотря на большее количество вызовов у нового фильтра, чем у строго, работает он быстрее.

Создадим новый файл filter_with_filename.py, в котором сразу в коде укажем имена файлов исходного и результирующего,
а также размер сетки 10 и количество градаций серого 50. После проверим его время выполнения.

До преоброзований в filter.py: 
![atl text](Pic/b1.PNG)
После преобразований в filter_with_filename.py, избавлены от консольного ввода:
![alt text](Pic/b2.PNG)

Результат работы профилирования filter_with_filename.py - 0.521 сек. 
![alt text](Pic/a3.PNG)

Тестовое изображение:
![alt text](input.JPG)
Результат работы изначального фильтра old_filter.py:
![alt text](res.jpg)
Результат работы фильтра filter.py (размер сетки - 10, количество градаций серого - 50):
![alt text](output.jpg)
Результат работы фильтра filter_with_filename.py (размер сетки - 10, количество градаций серого - 50):
![atl text](output2.jpg)

Через отладчик можно вывести все необходиммые свойства изображения и параметров:
![alt text](Pic/a4.PNG)
