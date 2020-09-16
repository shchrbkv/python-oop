# Часть 2

# Функция возвращает список из вещественных чисел
# поулченных из строки с пробелами-разделителями
def get_list():
    inp = input()
    return list(map(float, inp.split(" ")))

# Процедура получает список по ссылке и умножает на число
def multiply(arr, by):
    for i in range(0, len(arr)):
        arr[i] *= by

# Функция, возвраающая список, округлённый до двух знаков
def get_rounded_list(arr, by):
    return [round(x, by) for x in arr]

# Процедура сохранение в файл с выбранным именем (число на каждой новой строке)
def save_list_as(arr, name):
    with open(name+".txt", "w") as output:
        for num in arr:
            output.write(str(num) + "\n")

# Главная процедура с логикой программы
def main():
    print("Input number separated by space: ")
    nums = get_list()  # Для простого преобразования строки в список
    multiply(nums, 0.13)  # Для умножения вектора на число
    nums.sort()
    print("Rounded list:")
    print(get_rounded_list(nums, 2))  # Для простого округления
    save_list_as(get_rounded_list(nums, 2), "output-name")  # Для сохранения файла

# Вызов процедуры main
main()