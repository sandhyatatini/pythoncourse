from abc import ABC, abstractmethod
class Ride(ABC):
   def __init__(self,ride_id,user_name,pickup,drop,distance_km,fare_per_km,ride_cost,discount):
      self.__ride_id=ride_id
      self.__user_name=user_name
      self.__pickup=pickup
      self.__drop=drop
      self.__distance_km=distance_km
      self.__fare_per_km=fare_per_km
      self.__ride_cost=ride_cost
      self.__discount=discount
      self.status=("Confirmed", "Driver Assigned")
      self.ride_features={"Helmet", "Fast Pickup", "Live Tracking"}
      self.driver={
            "name": "Ravi Kumar",
            "contact": "9897393920",
            "vehicle": "TS06BX2787"
        }
   @abstractmethod
   def calculate_fare(self):
      pass
   def get_user_name(self):
      return self.__user_name
   def set_user_name(self,name):
      self.__user_name = name
   def get_ride_id(self):
      return self.__ride_id
   def get_distance(self):
      return self.__distance_km
   def get_fare_per_km(self):
      return self.__fare_per_km
   def get_discount(self):
       return self.__discount
   def get_ride_cost(self):
      return self.__ride_cost
   def display_ride_info(self):
        print("\nRide ID, User, Pickup, drop:", self.__ride_id, self.__user_name, self.__pickup, self.__drop, self.__ride_cost, sep=",")
        print("Discount applied: %.1f%%" % self.__discount)
        print(f"Total Distance: {self.__distance_km} km")
        print(f"Base fare: ${self.calculate_fare():.2f}")
        print(f"Discount: ${self.__discount:.2f}")
        print(f"Ride Type: {self.__class__.__name__}")
        print(f"Ride Status: {self.status[0]}")
        print(f"Ride Features: {', '.join(self.ride_features)}")
        print("Driver Details: Name - {name}, Contact - {contact}, Vehicle - {vehicle}".format(
            name=self.driver["name"],
            contact=self.driver["contact"],
            vehicle=self.driver["vehicle"]
        ))
class BikeRide(Ride):
   def calculate_fare(self):
      return (self.get_distance()*self.get_fare_per_km())*0.9
class AutoRide(Ride):
   def calculate_fare(self):
      return (self.get_distance()*self.get_fare_per_km())*0.95
class CabRide(Ride):
   def calculate_fare(self):
      return (self.get_distance()*self.get_fare_per_km())




