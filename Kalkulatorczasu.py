def add_time(start, duration, day=None):
    # Funkcja konwertująca czas dwunastogodzinny na dwudziestoczterogodzinny
    def to_24_hour(time):
        time, period = time.split()
        hours, minutes = map(int, time.split(':'))
        if period == "PM" and hours != 12:
            hours += 12
        return hours, minutes

    # Funkcja konwertująca czas dwudziestoczterogodzinny na dwunastogodzinny
    def to_12_hour(hours, minutes):
        period = "AM" if hours < 12 else "PM"
        if hours > 12:
            hours -= 12
        elif hours == 0:
            hours = 12
        return f"{hours}:{minutes:02d} {period}"

    start_hours, start_minutes = to_24_hour(start)
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Dodanie czasu
    new_hours = start_hours + duration_hours
    new_minutes = start_minutes + duration_minutes

    # Obsługa nadmiaru minut
    if new_minutes >= 60:
        new_hours += 1
        new_minutes -= 60

    # Obsługa dni
    days_passed = 0
    while new_hours >= 24:
        new_hours -= 24
        days_passed += 1

    # Dodanie dnia tygodnia
    if day is not None:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_index = (days_of_week.index(day.capitalize()) + days_passed) % 7
        new_time = f"{to_12_hour(new_hours, new_minutes)}, {days_of_week[day_index]}"
    else:
        new_time = to_12_hour(new_hours, new_minutes)

    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time

if __name__ == "__main__":
    print(add_time("3:30 PM", "2:12", "Monday"))
    print(add_time("2:59 AM", "24:00", "saturDay"))
    print(add_time("11:59 PM", "24:05", "Wednesday"))
    print(add_time("8:16 PM", "466:02", "tuesday"))
