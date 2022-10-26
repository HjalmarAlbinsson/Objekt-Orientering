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
        return(self.brand)

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
        return(self.color)
    def set_mileage(self, new_mileage):
        self.mileage = new_mileage
    def get_mileage(self):
        return(self.mileage)
    def get_modelyear(self):
        return(self.modelyear)
    


# ----------Huvudprogram----------
# Nu när klassen finns kan vi skapa objekt (variabler) med denna typ.
# Dessa objekt har också tillgång till klassens metoder (funktioner).
a_car = Car('Volvo', 'Blå', 1587, 1999)
b_car = Car("Mercedez","Röd", 1934, 1998)
print(a_car.get_brand())
print(b_car.get_brand())
print(a_car.get_color())
a_car.set_color("Grön")
print(a_car.get_color())
the_mileage = a_car.get_mileage()
print(the_mileage)
c_car = Car("Lamborghini", "Gul", 34, 2016)
d_car = Car("Bugatti", "Grön", 148, 2005)
my_cars = [a_car, b_car, c_car, d_car]
for car in my_cars:
    print(car.get_brand())

while 1 == 1:
    print("A-Z(1), Miltal(2), Årsmodel(3), Färg(4), Quit(q)")
    answer = input("Sorterings val: -> ")
    sort_list = []
    if answer == "1":
        for car in my_cars:
            sort_list.append(car.get_brand())
        sort_list.sort()
        for brand in sort_list:
            print(brand)
    elif answer == "2":
        for car in my_cars:
            sort_list.append(car.get_mileage())
        sort_list.sort()
        for mileage in sort_list:
            print(mileage)
    elif answer == "3":
        for car in my_cars:
            sort_list.append(car.get_modelyear())
        sort_list.sort()
        sort_list.reverse()
        for modelyear in sort_list:
            print(modelyear)
    elif answer == "4":
        for car in my_cars:
            sort_list.append(car.get_color())
        sort_list.sort()
        for color in sort_list:
            print(color)
    elif answer == "q":
        break
