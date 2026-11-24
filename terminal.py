from models import Habit, HabitManager


def main():
    manager = HabitManager()
    manager.load_habits()

    while True:
        print("\nVad vill du göra?")
        print("1. Visa dina vanor")
        print("2. Lägg till en vana")
        print("3. Återställ checkstatus")
        print("4. Spara vanor")
        print("5. Avsluta")

        choice = input("Välj ett alternativ [1-5]: ")
        habits = manager.get_habits()

        if choice == "1":
            if not habits:
                print("Du har inga vanor ännu.")
            else:
                for i, habit in enumerate(habits, start=1):
                    status = "klar" if habit.get_checked() else "inte klar"
                    print(f"{i}. {habit.get_name()} ({status})")

        elif choice == "2":
            name = input("Skriv en vana: ").strip()
            if name:
                manager.add_habit(Habit(name))
                manager.save_habits()
                print("Vanan är sparad.")
            else:
                print("Vanans namn får inte vara tomt.")

        elif choice == "3":
            for habit in habits:
                habit.set_checked(False)
            manager.save_habits()
            print("Checkstatusen har återställts för alla vanor.")

        elif choice == "4":
            manager.save_habits()
            print("Vanorna är sparade till habits.json.")

        elif choice == "5":
            manager.save_habits()
            print("Avslutar...")
            break

        else:
            print("Skriv en siffra mellan 1 och 6.")


if __name__ == "__main__":
    main()
