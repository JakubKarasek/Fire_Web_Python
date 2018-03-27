class Wektor(object):
    "Dwuwymiarowy wektor"

    def __init__(self, x, y):
        self.a = x
        self.b = y
        print("wektor został stworzony!")


    def dlugosc(self):
        "Zwraca długość wektora."
        return (self.a ** 2 + self.b ** 2) ** 0.5


w1 = Wektor(5, 7)  # pisze: wektor został stworzony!
print(w1.dlugosc())
