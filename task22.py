# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
print()
n_set = set()
m_set = set()
#n_set.add(1)
#print(f'n_set = {n_set}')
n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))
print()
print("Вводим значения первого множества: ================")
for i in range(n):
    n_inp = int(input(f'Введите элемент номер {i+1} первого множества: '))
    n_set.add(n_inp)
print()
print("Вводим значения второго множества: ================")
for i in range(m):
    m_inp = int(input(f'Введите элемент номер {i+1} второго множества: '))
    m_set.add(m_inp)
print()
print('исходные множества уникальных значений:')
print(f'n_set: {n_set}')
print(f'm_set: {m_set}')
#n_set = {2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2}
#m_set = {3, 6, 9, 12, 10, 8, 15, 18}
inter = list(n_set.intersection(m_set))
print('=========================================')
print(n_set)
print(m_set)
#print(inter)
min_num = inter[0]
min_pos = 0

for k in range(len(inter)-1):
    min_num = inter[k]
    min_pos = k
    
    for i in range(k,len(inter)):
        if inter[i] < min_num:
            min_pos = i
            min_num = inter[i]
        temp_min = min_num #сохранение мин. значения во временной переменной
        temp_pos = i #сохранение позиции минимального элемента
        inter[min_pos] = inter[k]
        inter[k] = temp_min
        
print(inter)