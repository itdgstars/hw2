n = int(input('Укажите размер списка: '))
n_list = input('Введите элементы списка через пробел: ').split()
arr = list(map(int, n_list))
x = int (input('Введите число X: '))
count = 0
for i in range(n):
    if arr[i] == x:
        count += 1
print(f'Число {x} встречается в списке {count} раз.')