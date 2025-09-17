# main.py
from ride_module import BikeRide, AutoRide, CabRide

def main():
    ride_id = int(input("Enter Ride ID: "))
    user_name = input("Enter your Name: ")
    pickup = input("Enter Pickup Location: ")
    drop = input("Enter Drop Location: ")
    distance_km = float(input("Enter Distance (in km): "))
    ride_type = input("Enter Ride Type (Bike/Auto/Cab): ").strip().lower()
    fare_per_km = int(input("Enter the fare per km: "))
    ride_cost = float(input("Enter Ride Cost: "))
    discount = float(input("Enter Discount Percentage: "))

    if ride_type == "bike":
        ride = BikeRide(ride_id, user_name, pickup, drop, distance_km, fare_per_km, ride_cost, discount)
    elif ride_type == "auto":
        ride = AutoRide(ride_id, user_name, pickup, drop, distance_km, fare_per_km, ride_cost, discount)
    else:
        ride = CabRide(ride_id, user_name, pickup, drop, distance_km, fare_per_km, ride_cost, discount)

    ride.display_ride_info()

if __name__ == "__main__":
    main()
