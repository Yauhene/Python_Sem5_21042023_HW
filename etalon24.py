print()
print('Ввод числа грядок:')
n = int(input())
print()
print('Ввод продуктивности:')
arr = list()
for i in range(n):
    print(f'продуктивность куста {i+1}')
    x = int(input())
    arr.append(x)
print('arr:', arr)
print()

arr_count = list()
for i in range(len(arr) - 1):
    print('Суммируем продуктивности и добавляем в arr_count:')
    arr_count.append(arr[i - 1] + arr[i] + arr[i +1])
    print(arr[i - 1], arr[i], arr[i +1],'----------------')
    print(arr_count, '++++++++++++++')

print('arr_count',arr_count)
arr_count.append(arr[-2] + arr[-1] + arr[0])
print('arr_count',arr_count)
print(max(arr_count))

