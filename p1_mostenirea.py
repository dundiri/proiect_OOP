# Definim clasa Phone
class Phone:
    name: str
    year: int
    turned_on = False
    screen_size: float


    def __init__(self, name, screen_size, year): # constructorul
        self.name = name
        self.screen_size = screen_size
        self.year = year


    def turn_on(self):
        if self.turned_on:
            print("Telefonul este deja pornit")
        else:
            print("Telefonul a fost pornit")
            self.turned_on = True


# telefon_oarecare =Phone()

#telefon_oarecare.turn_on()
#telefon_oarecare.turn_on()


def ring(self):
    print("Ring ring!")


def print_phone_properties(self):
    print(f"Nume: {self.name}")
    print(f"An fabricatie: {self.year}")
    print(f"Ecran: {self.screen_size}")
# Definim clasa AndroidPhone
# AndroidPhone este SUBCLASA a clasei Phone
# AndroidPhone EXTINDE clasa Phone
class AndroidPhone(Phone):
    android_version: float = None

    def set_android_version(self, version):
        self.android_version = version

    def print_android_version(self):
        if self.android_version:
            print(f"Telefonul are versiunea Android: {self.android_version}")
        else:
            print("Versiunea de Android nu a fost inca setata")

    # Definim clasa Iphone
    # Iphone este SUBCLASA a clasei Phone
    # Iphone EXTINDE clasa Phone


class Iphone(Phone):
    ios_version: float = None

    def set_ios_version(self, version):
        self.ios_version = version

    def print_ios_version(self):
        if self.ios_version:
            print(f"Telefonul are versiunea IOs: {self.ios_version}")
        else:
            print("Versiunea IOs nu a fost setata")




