# Проверка ресурсов системы для запущенного процесса

## Краткое описание проекта

Данный скрипт позволяет собрать статистику по ресурсам ОС для запущенного процесса

## Установка

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

## Как запустить

Для запуска проекта в консоли необходимо выполнить команду:

```
python3 main.py cpu_interval stats_frequency 
```
```cpu_interval``` - float, интервал для измерения процессорного времени. [Подробнее](https://psutil.readthedocs.io/en/latest/#psutil.Process.cpu_percent).

```stats_frequency``` - int, частота в секундах, с которой производятся новые замеры потребления ресурсов. 

## Сохранение результатов

После завершения процесса в директории программы появится файл Process utilization[время запуска процесса].json

