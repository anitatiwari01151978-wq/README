# Fitness Tracker App in Python
# Simple console-based application

class Workout:
    def __init__(self, activity, duration):
        self.activity = activity
        self.duration = duration
        self.calories = duration * 5

    def display(self):
        print(f"\nActivity : {self.activity}")
        print(f"Duration : {self.duration} mins")
        print(f"Calories : {self.calories}")


class FitnessTracker:
    def __init__(self):
        self.workouts = []

    def add_workout(self):
        activity = input("Enter activity name: ")
        duration = int(input("Enter duration (minutes): "))

        workout = Workout(activity, duration)
        self.workouts.append(workout)

        print("\nWorkout added successfully!")

    def view_workouts(self):
        if not self.workouts:
            print("\nNo workouts found.")
            return

        print("\n--- Workout History ---")
        for i, workout in enumerate(self.workouts, start=1):
            print(f"\nWorkout #{i}")
            workout.display()

    def total_calories(self):
        total = sum(workout.calories for workout in self.workouts)
        print(f"\nTotal Calories Burned: {total}")

    def menu(self):
        while True:
            print("\n===== Fitness Tracker =====")
            print("1. Add Workout")
            print("2. View Workouts")
            print("3. Total Calories")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_workout()

            elif choice == "2":
                self.view_workouts()

            elif choice == "3":
                self.total_calories()

            elif choice == "4":
                print("\nGoodbye!")
                break

            else:
                print("\nInvalid choice. Try again.")


# Run the app
tracker = FitnessTracker()
tracker.menu()