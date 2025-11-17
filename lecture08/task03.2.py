if __name__ == "__main__":
    car = Car("ABC-123", 142)

    # Accelerate the car
    car.accelerate(60)  # speed becomes 60 km/h

    # Drive for 1.5 hours
    car.drive(1.5)

    print(f"Current speed: {car.current_speed} km/h")
    print(f"Travelled distance: {car.travelled_distance} km")