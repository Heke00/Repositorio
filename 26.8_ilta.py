luku_temp = input("Anna minulle joku luku:\n")

try:
    luku = float(luku_temp)

    if luku.is_integer():
        print(f"Valitsemasi numero on {int(luku)} &")
    else:
        print(f"Valitsemasi numero on {luku} &")

    if luku < 100:
        print("lukusi on pienempi kuin 100!")

    elif luku > 100:
        print("lukusi on yli 100!")

    else:
        print("lukusi on sata!")


except ValueError:
    print("Vain numeroita kiitos!")