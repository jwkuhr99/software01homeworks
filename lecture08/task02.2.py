if __name__ == "__main__":
    car = Car("ABC-123", 142)

    # Step 1: Accelerations
    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)

    # Step 2: Print current speed
    print(f"Current speed after accelerations: {car.current_speed} km/h")

    # Step 3: Emergency brake
    car.accelerate(-200)

    # Step 4: Print final speed
    print(f"Final speed after emergency brake: {car.current_speed} km/h")