ride_id=int(input("Enter Ride ID: "))
user_name=input("Enter your Name: ")
pickup=input("Enter Pickup Location: ")
drop=input("Enter Drop Location: ")
distance_km=float(input("Enter Distance (in km): "))
categories_input=list(input("Enter Ride Type (e.g.,Bike,Auto,Cab): "))
fare_per_km=10.0
fare=distance_km*fare_per_km
ride_cost=float(input("Enter Ride Cost: "))
discount=float(input("Enter Discount Percentange: "))
status=("Confirmed","Driver Assigned")
ride_features=set(["Helmet","Fast Pickup","Live Tracking"])
driver={
    "name":"Ravi Kumar",
    "contact":"9897393920",
    "vehicle":"TS06BX2787"
}
#1.Comma Separation
print("\nRide ID, User, Pickup, drop:",ride_id, user_name, pickup, drop, sep=",")
#2.Percentage formating
print("Discount applied: %.1f%%"%discount)
#3.f-string
print(f"Total Distance:{distance_km} km")
print(f"Base fare:${fare:.2f}")
print(f"Discount:${discount:.2f}")
print(f"Ride Type: {categories_input[0]}")
print(f"Ride Status: {status[0]}")
print(f"Ride Features:{', '.join(ride_features)}")
#4.format()
print("Driver Details: Name - {name}, Contact - {contact}, Vehicle - {vehicle}".format(
    name=driver["name"],
    contact=driver["contact"],
    vehicle=driver["vehicle"]
))




