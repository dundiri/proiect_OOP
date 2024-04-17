from abc import ABC, abstractmethod


'''
Presupun ca se organizeaza competitii la nivel de scoala. 
Implementez solutia pentru competitii in oricare din clase, 
incercand sa aplica si celelalte concepte de mostenire si abstractizare si polimorfism
'''
#olimpiade

class Gradinita(ABC):
    def __init__(self):
         self.info_elevi = {}
    @abstractmethod
    def activitate_practica(self):
        pass

    @abstractmethod
    def ora_de_somn(self):
        raise NotImplementedError("Nu ai implementat metoda")

    @abstractmethod
    def olimpiada(self):
        raise NotImplementedError("Nu sunt olimpiade in scoala")

    class G_Private1(Gradinita):
        __detalii_elevi = dict()
        matematicieni = None

        @property
        def detalii_elevi(self):
            return self.__detalii_elevi

        @detalii_elevi.getter
        def detalii_elevi(self):
            return self.__detalii_elevi

        @detalii_elevi.deleter
        def detalii_elevi(self):
            self.__detalii_elevi.clear()

        @detalii_elevi.setter
        def detalii_elevi(self, detalii):
            for key, value in detalii.items():
                if int(value["varsta"]) >= 8:
                    print("Prea batran pentru gradinita")
                else:
                    self.__detalii_elevi.update(detalii)

        def activitate_practica(self):
            print("Elevii joaca darts ->")

        def ora_de_somn(self):
            print("Copii dorm de la 14:00 la 15:00")

            def olimpiada(self, *args):  # (1, 6, 4)
                print("Super olimpiada la matematica")
                self.matematicieni = self.nr_elevi() / 2
                print(f'Numar concurenti: {self.matematicieni}')
                numere = len(args)
                suma = 0
                for arg in args:
                    suma = suma + int(arg)
                media = suma / numere
                print(f"Media Aritmetica este: {media}")
                print(f'Media a fost calculata cu succes de: {self.matematicieni / 2} elevi')


