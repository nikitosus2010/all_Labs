class Restaurant:
    def __init__(self, restaurant_name, cuisine_type,rate):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rate = rate

    def describe_restaurant(self):
        print("Название ресторана:", self.restaurant_name)
        print("Тип кухни:", self.cuisine_type)
        print("Рейтинг:", self.rate)

    def open_restaurant(self):
        print("Ресторан", self.restaurant_name,"Открыт")
    def rateup(self, nrate):
        self.rate=nrate


NewRestaurant = Restaurant(input("Введите название:"), input("Введите тип кухни:"), input("Введите рейтинг:"))
NewRestaurant.describe_restaurant()
NewRestaurant.rateup(input("Введите новый рейтинг:"))
NewRestaurant.describe_restaurant()


Restaurant1 = Restaurant(input("Введите название:"), input("Введите тип кухни:"), input("Введите рейтинг:"))
Restaurant2 = Restaurant(input("Введите название:"), input("Введите тип кухни:"), input("Введите рейтинг:"))
Restaurant3 = Restaurant(input("Введите название:"), input("Введите тип кухни:"), input("Введите рейтинг:"))


Restaurant1.describe_restaurant()
Restaurant2.describe_restaurant()
Restaurant3.describe_restaurant()