my_poslidovnist=input("Введіть послідовність чисел розділені пробілами")
number=my_poslidovnist.split()
num=set(number)
if len(number)==len(num):
    print("is unique sequence")
else:
    print("duplicate list")