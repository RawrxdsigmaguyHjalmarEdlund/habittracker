import json


class Habit:
    def __init__(self, name: str, checked: bool = False):
        self._name = name
        self._checked = checked

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_checked(self) -> bool:
        return self._checked

    def set_checked(self, checked: bool) -> None:
        self._checked = checked

    def check_in(self) -> None:
        self._checked = True


class HabitManager:
    def __init__(self, filename: str = "habits.json"):
        self._habits: list[Habit] = []
        self._filename = filename

    def get_habits(self) -> list[Habit]:
        return list(self._habits)

    def add_habit(self, habit: Habit) -> None:
        self._habits.append(habit)

    def clear_habits(self) -> None:
        self._habits.clear()

    def save_habits(self) -> None:
        data = [
            {"name": habit.get_name(), "checked": habit.get_checked()}
            for habit in self._habits
        ]
        with open(self._filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def load_habits(self) -> None:
        try:
            with open(self._filename, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            self._habits = []
            return

        self._habits = [
            Habit(item["name"], item.get("checked", False)) for item in data
        ]
