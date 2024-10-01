#!/usr/bin/env python3

import os  # Импортируем модуль os для работы с файловой системой

def analyze_directory(path):
    # Создаем функцию и в ней пустой список, куда будут помещаться файлы и дериктории
    items = []

    # Проходим по каждому элементу в текущей директории
    for item in os.listdir(path):
        # Получаем полный путь к элементу (файлу или директории)
        full_path = os.path.join(path, item)

        # Получаем размер элемента
        size = os.path.getsize(full_path)
        # Добавляем имя элемента и его размер в список
        items.append((item, size))

    # Сортируем список по размеру в порядке убывания
    items.sort(key=lambda x: x[1], reverse=True)

    for name, size in items:
        print(f"{name}: {size} байт")  # Выводим имя файла или директории и его размер

if __name__ == "__main__":
    current_directory = os.getcwd()  # Получаем путь к текущей директории
    analyze_directory(current_directory)  # Вызываем функцию для анализа текущей директории
