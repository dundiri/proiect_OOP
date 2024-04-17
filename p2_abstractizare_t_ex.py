from abc import ABC, abstractmethod
# Definim clasa abstracta Animal, care va fi o interfata
# Clasa Animal devine abstracta prin extinderea lui ABC (Clasa de baza abstracta)
class Animal(ABC):

    # Definim o proprietate abstracta <<sange>>
    # Atentie! Aceasta va fi o proprietate (atribut/field)
    # Desi seamana cu definirea unei metode, in clasele care vor extinde clasa Animal, <<sange>> va fi o proprietate
    # Pentru a defini proprietati abstracte, folosim decoratorul @property urmat de @abstractmethod (in ordinea asta)
    # Astfel obligam clasele care extind clasa Animal sa contina un atribut (field/proprietate) cu numele sange
    @property  # decorator care anunta ca este vorba de o proprietate (adica atribut/field)
    @abstractmethod  # anunta ca metoda (in cazul de fata proprietatea) abstracta, deci trebuie implementata in subclasa
    def sange(self):
        pass  # pass se poate folosi in acest caz, pentru a marca faptul ca aici nu este necesara o implementare

    # Definim inca o proprietate abstracta: <<nume>>
    @property
    @abstractmethod
    def nume(self):
        pass

    @abstractmethod
    def scoate_sunet(self):
        pass

    # In Python putem avea si implementari default in clase abstracte.
    def print_proprietati(self):
        print(f'Animalul {self.nume} are sangele {self.sange}')


# Declaram clasa <<Pisica>>
# Aceasta mosteneste proprietatile de la clasa Mamifer si este obligata sa implementeze tot din clasa Animal
class Pisica(Animal):
    nume = "pisica"
    sange = "cald"

    def scoate_sunet(self):
        print("Pisica face miau")
class Sarpe(Animal):
    nume = "sarpe"
    sange = "rece"

    def scoate_sunet(self):
        print("Sarpele face sssSSSss")
# Instantiem un obiect de tip Pisica()


pisica_obiect = Pisica()
pisica_obiect.scoate_sunet()
pisica_obiect.print_proprietati()
# Verificam daca clasa Pisica este o subclasa a clasei Animal (adica daca mosteneste din clasa Animal)
print(f"Clasa <<Pisica>> este o subclasa a clasei <<Animal>>: {issubclass(Pisica, Animal)}")

# Verificam daca obiectul pisica_obiect este o instanta a clasei Animal
print(f"Obiectul <<pisica_obiect>> este o instanta a clasei <<Animal>>: {isinstance(pisica_obiect, Animal)}")

# Verificam daca obiectul pisica_obiect este o instanta a clasei Pisica
print(f"Obiectul <<pisica_obiect>> este o instanta a clasei <<Pisica>>: {isinstance(pisica_obiect, Pisica)}")

print("-----------------------------------")

sarpe_obiect = Sarpe()
sarpe_obiect.scoate_sunet()
sarpe_obiect.print_proprietati()

# Verificam daca clasa Sarpe este o subclasa a clasei Animal (adica daca mosteneste din clasa Animal)
print(f"Clasa <<Sarpe>> este o subclasa a clasei <<Animal>>: {issubclass(Sarpe, Animal)}")

# Verificam daca obiectul sarpe_obiect este o instanta a clasei Animal
print(f"Obiectul <<sarpe_obiect>> este o instanta a clasei <<Animal>>: {isinstance(sarpe_obiect, Animal)}")

# Verificam daca obiectul sarpe_obiect este o instanta a clasei Sarpe
print(f"Obiectul <<sarpe_obiect>> este o instanta a clasei <<Sarpe>>: {isinstance(sarpe_obiect, Sarpe)}")

# Verificam daca clasa Sarpe este o subclasa a clasei Pisica (adica daca mosteneste din clasa Pisica)
print(f"Clasa <<Sarpe>> este o subclasa a clasei <<Animal>>: {issubclass(Sarpe, Pisica)}")

