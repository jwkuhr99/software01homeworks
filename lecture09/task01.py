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


# Test the class
if __name__ == "__main__":
    h = Elevator(0, 10)  # elevator from floor 0 to 10

    h.go_to_floor(5)  # move to the fifth floor
    h.go_to_floor(0)  # move back to the bottom floor