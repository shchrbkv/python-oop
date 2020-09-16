# Часть 1

# Ввод чисел с разделителем-пробелом
print("Input number separated by space: ")
inp = input()

# Добавление в список путём деления входной строки
# и парсинга чисел в тип float с помощью map()
nums = list(map(float, inp.split(" ")))

# Умножение чисел на 0.13 и сохранение в новый список
nums_mp = [x*0.13 for x in nums]

# Сортировка списка по возрастанию
nums_mp.sort()

# Печать списка с округлением до двух знаков
print("Rounded list:")
for num in nums_mp:
    print("{:.2f}".format(num))

# Сохранение в файл (число на каждой новой строке)
with open("output.txt", "w") as output:
    for num in nums_mp:
        output.write("{:.2f}".format(num)+"\n")
