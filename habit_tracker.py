import json
import os
from datetime import datetime

# File to store the habit data
HABITS_FILE = 'habits.json'

# Load habits from file
def load_habits():
    if os.path.exists(HABITS_FILE):
        with open(HABITS_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save habits to file
def save_habits(habits):
    with open(HABITS_FILE, 'w') as file:
        json.dump(habits, file, indent=4)

# Add a new habit
def add_habit(habits, habit_name):
    if habit_name in habits:
        print(f'Habit "{habit_name}" already exists!')
    else:
        habits[habit_name] = {"streak": 0, "last_completed": None}
        save_habits(habits)
        print(f'Added new habit: "{habit_name}"')

# Mark a habit as complete for today
def complete_habit(habits, habit_name):
    if habit_name not in habits:
        print(f'Habit "{habit_name}" does not exist.')
        return
    
    today = datetime.now().date().isoformat()
    last_completed = habits[habit_name]["last_completed"]

    if last_completed == today:
        print(f'Habit "{habit_name}" is already marked as completed today.')
    else:
        # If last completed was yesterday, increase the streak; otherwise, reset it
        if last_completed == (datetime.now().date().replace(day=datetime.now().day-1)).isoformat():
            habits[habit_name]["streak"] += 1
        else:
            habits[habit_name]["streak"] = 1

        habits[habit_name]["last_completed"] = today
        save_habits(habits)
        print(f'Great job! Habit "{habit_name}" marked as complete. Current streak: {habits[habit_name]["streak"]}')

# View all habits and their streaks
def view_habits(habits):
    if not habits:
        print("No habits tracked yet.")
        return
    
    print("\n--- Habit Tracker ---")
    for habit, data in habits.items():
        streak = data["streak"]
        last_completed = data["last_completed"] or "Never"
        print(f'{habit}: Streak - {streak} | Last Completed - {last_completed}')
    print()

# Delete a habit
def delete_habit(habits, habit_name):
    if habit_name in habits:
        del habits[habit_name]
        save_habits(habits)
        print(f'Habit "{habit_name}" has been deleted.')
    else:
        print(f'Habit "{habit_name}" does not exist.')

# Command line interface
def main():
    habits = load_habits()

    while True:
        print("\n--- Habit Tracker Menu ---")
        print("1. Add a new habit")
        print("2. Complete a habit for today")
        print("3. View all habits")
        print("4. Delete a habit")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            habit_name = input("Enter the habit name: ")
            add_habit(habits, habit_name)

        elif choice == '2':
            habit_name = input("Enter the habit to mark as complete: ")
            complete_habit(habits, habit_name)

        elif choice == '3':
            view_habits(habits)

        elif choice == '4':
            habit_name = input("Enter the habit to delete: ")
            delete_habit(habits, habit_name)

        elif choice == '5':
            print("Goodbye! Keep up with your habits!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
