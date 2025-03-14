# fix_poem.py
with open('pushkin_poem.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Заменяем последнюю строку
if lines:
    lines[-1] = 'ЭТООНОВАЯ СТРОКА\n'

# Записываем изменения обратно в файл
with open('pushkin_poem.txt', 'w', encoding='utf-8') as file:
    file.writelines(lines)