class Customer:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def __init__(self):

    def set_name(self,name):
      self.name = name 
    def get_name(self):
      return self.name

    def set_age(self,age):
      self.age = age
    def get_age(self):
      return self.age


class MainBikeRental:
      def __init__(self):
        self.num_of_bikes = []
        self.num_of_rentals = []

      def set_bikes(self,num_of_bikes):
        self.num_of_bikes = num_of_bikes
      def get_bikes(self):
        return self.num_of_bikes

      def set_rentals(self,num_of_rentals):
        self.num_of_rentals = num_of_rentals
      def get_rentals(self):
        return self.num_of_rentals

      def requestBike(self,age,num_of_bikes):
        if (age <= 6):
          print("you must be more that 6 years")

          return

        available_bikes = len(self.num_of_bikes)
        if num_of_bikes <= available_bikes:
            for _ in range(num_of_bikes):
              self.num_of_rentals.append((num_of_bikes))
            print(f"{num_of_bikes} bikes rented, take it :)")      
        else:
            print("please wait 10 minutes")
                 

      def returnBike(self,rentalTime, num_of_bikes):
        bill_cost = rentalTime * 40
        for _ in range(num_of_bikes):
            self.num_of_bikes.append("returned bike")
            print(f"{num_of_bikes} bikes returned")
        print(f"your total cost is: {bill_cost}")


      def addBike(self,num_of_bikes):
        self.num_of_bikes.append(num_of_bikes)   

      def totalCost(self):
        total_cost = 0
        for bike in self.num_of_bikes:
          total_cost += bike.price
          return total_cost

class Bike:
  def __init__(self,name,price):
    self.name = name
    self.price = price 

  def set_name(self,name):
    self.name = name
  def get_name(self):
    return self.name

  def set_price(self,price):
    self.price = price
  def get_price(self):
    return self.price 

class electricBike(Bike):
  def __init__(self,maxspeed):
    self.maxspeed = maxspeed

  def set_maxspeed(self,maxspeed):
    self.maxspeed = maxspeed
  def get_maxspeed(self):
    return self.maxspeed

class normalBike(Bike):
  def __init__(self,maxspeed):
    self.maxspeed = maxspeed

  def set_maxspeed(self,maxspeed):
    self.maxspeed = maxspeed
  def get_maxspeed(self):
    return self.maxspeed
