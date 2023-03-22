# zadanie 1
# import random
# plikon=open('bruther.txt','w')
# for i in range(0,10):
#     x=random.randint(0,30)
#     y=x*2
#     plikon.write(str(y))
#     plikon.write('\n')
# #zadanie 2
# plikon.close()
# plikof=open('bruther.txt','r')
# print(plikof.readlines())
# zadanie 3
with open("tekst.txt", "r+") as plik:
    plik.write('Szły pchły koło wody')
    plik.write('pchła pchłę pchła do wody')
    plik.write('a ta pchła płakała')
    print(plik.readlines())
#zadanie 4
class Nazakupy:
    """Wszystko potrzebne do udanych zakupów"""
    zakupson=412
    # def __init__(self, nazwa, ilosc, price, jednostka_miary, cena_jednostkowa):
    #     self.nazwa=nazwa
    #     self.ilosc=ilosc
    #     self.price=price
    #     self.jednostka_miary=jednostka_miary
    #     self.cena_jednostkowa=cena_jednostkowa
    # nazwa='jako'
    # ilosc=7
    # cena=8
    # jednostka_miary='sztuka'
    # cena_jednostkowa=cena/ilosc
    def konwencja(self):
        return 0
    def __init__(self, ilosc, nazwa, price):
        self.nazwa = nazwa
        self.ilosc = ilosc
        self.price=price
        self.jednostka_miary = 'sztuk'
        self.cena_jednostkowa = price / ilosc
    def ilekosztuje(self):
        print(self.cena*self.ilosc)
    def wyswietlprodukt(self):
        print(self.nazwa)
        print(self.cena)
        print(self.ilosc)
    def ile(self):
        print(self.ilosc, self.jednostka_miary)

obiekt=Nazakupy(10,'dupa',69)
print(obiekt.zakupson)
obiekt.ilekosztuje()
obiekt.ile()
class arytmetyka():
    def pobierz_elementy(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z



