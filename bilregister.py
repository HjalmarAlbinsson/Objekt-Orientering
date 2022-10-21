class Car():
    '''
    En klass som håller reda på några egenskaper hos en bil.
    '''
    # Metoden __init__, körs alltid då ett objekt skapas

    def __init__(self, brand, color, mileage, modelyear):
        # Nedanstående variabler kallas för attribut.
        # Alla objekt av klassen Car har egna värden på dessa.
        self.brand = brand
        self.color = color
        self.mileage = mileage
        self.modelyear = modelyear

    def get_brand(self):
        '''
        Skriver ut bilmärket
        '''
        print(self.brand)

    def set_brand(self, new_brand):
        '''
        Parameter: new_brand | sträng
        Uppdaterar bilmärket om det existerar. Om det inte existerar
        så tilldelas aktuellt objekt märket enligt parametern.
        '''
        self.brand = new_brand
    def set_color(self, new_color):
        self.color = new_color
    def get_color(self):
        print(self.color)
    def set_mileage(self, new_mileage):
        self.mileage = new_mileage
    def get_mileage(self):
        return(self.mileage)
    


# ----------Huvudprogram----------
# Nu när klassen finns kan vi skapa objekt (variabler) med denna typ.
# Dessa objekt har också tillgång till klassens metoder (funktioner).
a_car = Car('Volvo', 'Blå', 1587, 1999)
b_car = Car("Mercedez","Röd", 1934, 1998)
a_car.get_brand()
b_car.get_brand()
a_car.get_color()
a_car.set_color("Grön")
a_car.get_color()
the_mileage = a_car.get_mileage()
print(the_mileage)
c_car = Car("Lamborghini", "Gul", 34, 2016)
d_car = Car("Bugatti", "Grön", 148, 2005)
my_cars = [a_car, b_car, c_car, d_car]
for car in my_cars:
    print(car.get_brand())

print("A-Z(1), Miltal(2), Årsmodel(3), Färg(4)")
answer = input("Sorterings val: -> ")
if answer == "1":
    for car in my_cars:
        
