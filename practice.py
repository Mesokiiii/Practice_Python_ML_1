"""
Практическая работа №1
Тема: Базовые структуры данных, файловый ввод-вывод и сериализация данных в Python.
Курс: 2 курс, 1 семестр.
"""

from pathlib import Path
import json
import pickle
import sys

# Гарантируем корректный вывод UTF-8 в терминале Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# Базовая директория для сохранения временных файлов задания
BASE_DIR = Path(__file__).resolve().parent


# =====================================================================
# Задание 1. Базовые операции со срезами и разбиением строк
# =====================================================================
def task1_slices_and_join():
    print("--- Задание 1: Срезы и сборка строк ---")
    source_list = [115, 202, 192, 334, 257]
    slice_result = source_list[:4]
    print(f"Исходный список: {source_list}")
    print(f"Срез [:4]: {slice_result}")

    text = "this is important"
    words = text.split()
    joined_text = "".join(words)
    print(f"Исходная строка: '{text}'")
    print(f"Разбиение .split(): {words}")
    print(f"Склейка ''.join(): '{joined_text}'\n")


# =====================================================================
# Задание 2. Формирование строки из двух первых и двух последних символов
# =====================================================================
def task2_first_last_chars(s: str) -> None:
    print("--- Задание 2: Первые и последние два символа строки ---")

    # Способ 1: Явное ветвление if-else
    def solution_1(val: str) -> str:
        if len(val) < 2:
            return ""
        return val[:2] + val[-2:]

    # Способ 2: Тернарный условный оператор
    def solution_2(val: str) -> str:
        return val[:2] + val[-2:] if len(val) >= 2 else ""

    # Способ 3: Форматированная f-строка
    def solution_3(val: str) -> str:
        if len(val) >= 2:
            return f"{val[:2]}{val[-2:]}"
        return ""

    print(f"Тестовая строка: '{s}'")
    print(f"Способ 1 (if-else):   '{solution_1(s)}'")
    print(f"Способ 2 (тернарный): '{solution_2(s)}'")
    print(f"Способ 3 (f-строка):  '{solution_3(s)}'")

    short_str = "A"
    print(f"Короткая строка '{short_str}' -> '{solution_1(short_str)}' (длина < 2)\n")


# =====================================================================
# Задание 3. Поэлементное масштабирование списка на скаляр
# =====================================================================
def task3_list_multiplication(numbers: list[int], factor: int) -> None:
    print("--- Задание 3: Умножение элементов списка на число ---")

    # Способ 1: Пошаговое добавление в новый список через .append()
    def solution_append(nums: list[int], mult: int) -> list[int]:
        result = []
        for x in nums:
            result.append(x * mult)
        return result

    # Способ 2: Модификация элементов копии списка по индексам
    def solution_inplace(nums: list[int], mult: int) -> list[int]:
        numbers_copy = nums.copy()
        for i in range(len(numbers_copy)):
            numbers_copy[i] *= mult
        return numbers_copy

    # Способ 3: Генератор списка (List Comprehension - классический Python-подход)
    def solution_comprehension(nums: list[int], mult: int) -> list[int]:
        return [x * mult for x in nums]

    print(f"Исходный список: {numbers}, множитель: {factor}")
    print(f"Способ 1 (append):        {solution_append(numbers, factor)}")
    print(f"Способ 2 (по индексам):   {solution_inplace(numbers, factor)}")
    print(f"Способ 3 (comprehension): {solution_comprehension(numbers, factor)}\n")


# =====================================================================
# Задание 4. Объединение трех словарей в один
# =====================================================================
def task4_dict_merge() -> None:
    print("--- Задание 4: Объединение трех словарей ---")
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}
    d3 = {"e": 5, "f": 6}

    # Способ 1: Оператор объединения '|' (доступен с Python 3.9)
    def solution_pipe(dict1: dict, dict2: dict, dict3: dict) -> dict:
        return dict1 | dict2 | dict3

    # Способ 2: Метод .update() на копии словаря
    def solution_update(dict1: dict, dict2: dict, dict3: dict) -> dict:
        result = dict1.copy()
        result.update(dict2)
        result.update(dict3)
        return result

    print(f"dict1: {d1}, dict2: {d2}, dict3: {d3}")
    print(f"Способ 1 (оператор '|'):  {solution_pipe(d1, d2, d3)}")
    print(f"Способ 2 (метод update): {solution_update(d1, d2, d3)}\n")


# =====================================================================
# Задание 5. Добавление элемента в неизменяемый кортеж
# =====================================================================
def task5_tuple_append() -> None:
    print("--- Задание 5: Добавление элемента к кортежу ---")
    source_tuple = (1, 2, 3)
    new_item = 777

    # Способ 1: Конкатенация с одноэлементным кортежем
    def solution_concat(tpl: tuple, item: int) -> tuple:
        return tpl + (item,)

    # Способ 2: Преобразование в список, модификация и обратная конвертация
    def solution_list_cast(tpl: tuple, item: int) -> tuple:
        temp_list = list(tpl)
        temp_list.append(item)
        return tuple(temp_list)

    print(f"Исходный кортеж: {source_tuple}, добавляемый элемент: {new_item}")
    print(f"Способ 1 (конкатенация кортежей): {solution_concat(source_tuple, new_item)}")
    print(f"Способ 2 (приведение через list): {solution_list_cast(source_tuple, new_item)}\n")


# =====================================================================
# Задание 6. Файловый ввод-вывод и подсчет строк
# =====================================================================
def task6_file_io() -> None:
    print("--- Задание 6: Запись, чтение и подсчет строк в файле ---")
    test_file = BASE_DIR / "test.txt"

    # Создание/перезапись файла тестовыми данными
    lines_to_write = ["Первая строка\n", "Вторая строка\n", "Третья строка (добавленная)\n"]
    with open(test_file, "w", encoding="utf-8") as f:
        f.writelines(lines_to_write)

    # Дозапись в конец файла (режим 'a')
    with open(test_file, "a", encoding="utf-8") as f:
        f.write("Четвертая строка (режим append)\n")

    # Чтение содержимого
    with open(test_file, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"Содержимое файла {test_file.name}:")
    print(content.strip())

    # Подсчет строк. Способ 1: через readlines()
    def count_lines_readlines(path: Path) -> int:
        with open(path, "r", encoding="utf-8") as f:
            return len(f.readlines())

    # Подсчет строк. Способ 2: итерация по файловому объекту (эффективно по памяти)
    def count_lines_iter(path: Path) -> int:
        count = 0
        with open(path, "r", encoding="utf-8") as f:
            for _ in f:
                count += 1
        return count

    print(f"Подсчет через len(f.readlines()): {count_lines_readlines(test_file)}")
    print(f"Подсчет через построчную итерацию: {count_lines_iter(test_file)}\n")


# =====================================================================
# Задание 7. Сериализация и десериализация бинарных данных (Pickle)
# =====================================================================
def task7_pickle_serialization() -> None:
    print("--- Задание 7: Сериализация объектов модулем pickle ---")
    data = [10, 20, "Привет", 3.14]
    pkl_file = BASE_DIR / "data.pkl"

    # Способ 1: С контекстным менеджером 'with'
    def solution_with_context(data_to_save: list, path: Path) -> list:
        with open(path, "wb") as f:
            pickle.dump(data_to_save, f)
        with open(path, "rb") as f:
            return pickle.load(f)

    # Способ 2: Явное открытие и закрытие дескриптора файла
    def solution_explicit_close(data_to_save: list, path: Path) -> list:
        f_write = open(path, "wb")
        pickle.dump(data_to_save, f_write)
        f_write.close()

        f_read = open(path, "rb")
        loaded = pickle.load(f_read)
        f_read.close()
        return loaded

    print(f"Исходные данные: {data}")
    res1 = solution_with_context(data, pkl_file)
    res2 = solution_explicit_close(data, pkl_file)
    print(f"Способ 1 (контекстный менеджер with): {res1}")
    print(f"Способ 2 (явные open/close):          {res2}")
    print(f"Проверка эквивалентности: {res1 == data}\n")


# =====================================================================
# Задание 8. Сериализация и десериализация структурированных данных (JSON)
# =====================================================================
def task8_json_serialization() -> None:
    print("--- Задание 8: Сериализация в формат JSON ---")
    data = {"name": "Ivan", "age": 20, "course": 2, "semester": 1}
    json_file = BASE_DIR / "data.json"

    # Способ 1: Прямая запись/чтение через файловый поток (json.dump / json.load)
    def solution_stream(obj: dict, path: Path) -> dict:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=2)
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    # Способ 2: Преобразование в строку и последующая запись (json.dumps / json.loads)
    def solution_string(obj: dict, path: Path) -> dict:
        serialized_str = json.dumps(obj, ensure_ascii=False)
        with open(path, "w", encoding="utf-8") as f:
            f.write(serialized_str)
        with open(path, "r", encoding="utf-8") as f:
            return json.loads(f.read())

    print(f"Исходный словарь: {data}")
    res1 = solution_stream(data, json_file)
    res2 = solution_string(data, json_file)
    print(f"Способ 1 (json.dump / json.load):   {res1}")
    print(f"Способ 2 (json.dumps / json.loads): {res2}")
    print(f"Проверка эквивалентности: {res1 == data}\n")


def main():
    print("=" * 60)
    print("ПРАКТИЧЕСКАЯ РАБОТА №1 | 2 КУРС, 1 СЕМЕСТР")
    print("Основы языка Python: структуры данных, файлы и сериализация")
    print("=" * 60 + "\n")

    task1_slices_and_join()
    task2_first_last_chars("Машина")
    task3_list_multiplication([10, 15, 30, 15], 9)
    task4_dict_merge()
    task5_tuple_append()
    task6_file_io()
    task7_pickle_serialization()
    task8_json_serialization()

    print("=" * 60)
    print("Все задания успешно выполнены.")
    print("=" * 60)


if __name__ == "__main__":
    main()