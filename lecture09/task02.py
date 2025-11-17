class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")
        else:
            print("Already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")
        else:
            print("Already at the bottom floor.")

    def go_to_floor(self, target):
        if target < self.bottom or target > self.top:
            print("Invalid floor.")
            return

        print(f"Moving to floor {target}...")

        while self.current_floor < target:
            self.floor_up()

        while self.current_floor > target:
            self.floor_down()


class Building:
    def __init__(self, bottom, top, num_elevators):
        self.elevators = []
        for _ in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, target_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"\nRunning elevator {elevator_number}...")
            self.elevators[elevator_number].go_to_floor(target_floor)
        else:
            print("Invalid elevator number.")


# Main program
if __name__ == "__main__":
    building = Building(0, 10, 3)  # bottom=0, top=10, 3 elevators

    building.run_elevator(0, 5)   # run elevator 0 to floor 5
    building.run_elevator(1, 8)   # run elevator 1 to floor 8
    building.run_elevator(0, 0)   # bring elevator 0 back to bottom