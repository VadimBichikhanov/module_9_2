first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

#  список, состоящий из длин строк из first_strings, но только если длина строки не менее 5 символов.
first_result = [len(s) for s in first_strings if len(s) >= 5]

# список кортежей, где каждая пара состоит из слов одинаковой длины из first_strings и second_strings.
second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]

# словарь, где ключом будет строка, а значением — длина строки. Строки будут браться из объединенных списков first_strings и second_strings, но только если длина строки четная.
all_strings = first_strings + second_strings
third_result = {s: len(s) for s in all_strings if len(s) % 2 == 0}

# Вывод результатов
print(f'first_result:\n {first_result}')
print(f'second_result:\n {second_result}')
print(f'third_result:\n {third_result}')