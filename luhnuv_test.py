cislo_karty = "49927398716"
print(cislo_karty)


def je_karta_platna():

    print("otoceni", revers(y=cislo_karty))
    print("suda cisla", sud_cisla())
    print("licha cisla", lich_cisla())
    print("sum licha cisla", sum_lich_cisla())
    print("sum suda cisla ", sum_suda())
    print(je_platna())


def revers(y):
    return y[::-1]


def sud_cisla():
    return revers(cislo_karty)[1::2]


def lich_cisla():
    return revers(cislo_karty)[0::2]


def sum_lich_cisla():
    sum_lich = [int(i) for i in lich_cisla()]
    return sum(sum_lich)


def suda_to_int():
    sud_int = [int(i) for i in sud_cisla()]
    return sud_int


def sum_suda():
    return sum(sum(divmod(d * 2, 10)) for d in suda_to_int())


def je_platna():
    sum_dohromady = sum_suda() + sum_lich_cisla()
    if sum_dohromady % 10 == 0:
        print("Karta je platná.")
        return True
    else:
        print("Karta je neplatná!")
        return False


je_karta_platna()
