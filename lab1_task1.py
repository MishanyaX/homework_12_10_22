#task 1
while True:
    print("Vvedite oklad sotrudnika:")
    try:
        a = int(input())
        if a <= 0:
            print("Oklad ne moget bitb otrizatelnim i 0!")
            continue
        break
    except ValueError:
        print("Vvod dolgen predstavlyat chislo!")
b = a * 2 / 3 * 0.87
print("Summa, vidavaemaya na ruki sotrudniku: ", int(b))