my_poslidovnist=input("Введіть послідовність чисел розділені пробілами")
my_poslidovnist1=input("Введіть другу послідовність чисел розділені пробілами")
number=set(my_poslidovnist.split())
rebmun=set(my_poslidovnist1.split())
all_poslidovnist=number & rebmun
if all_poslidovnist:
    print("Спільні елементи у двох послідовностях:", all_poslidovnist)
else:
    print("Немає спільних елементів у данних послідовностях")