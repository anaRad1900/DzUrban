example = 'Топинамбур'

# Выводим первый символ строки
print(example[0])  # Ожидаемый результат: Т

# Выводим последний символ строки, используя отрицательный индекс
print(example[-1])  # Ожидаемый результат: р

# Выводим вторую половину строки
middle_index = len(example) // 2
second_half = example[middle_index:]
print(second_half)  # Ожидаемый результат: амбур

# Выводим строку наоборот
reversed_example = example[::-1]
print(reversed_example)  # Ожидаемый результат: рубманипоТ

# Выводим каждый второй символ строки
every_second_char = example[1::2]
print(every_second_char)  # Ожидаемый результат: оиабр
