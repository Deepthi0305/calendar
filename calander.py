# calendar_app.py

import calendar
import datetime
import os

def show_calendar(year, month):
    print("\n" + calendar.month(year, month))

def save_calendar_to_file(year, month, filename="calendar_output.txt"):
    with open(filename, "w") as f:
        f.write(calendar.month(year, month))
    print(f"✅ Calendar saved to {filename}")

def main():
    today = datetime.date.today()
    year = today.year
    month = today.month

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("📅 PYTHON CALENDAR APP\n")
        show_calendar(year, month)

        print("Options:")
        print("1. Next Month")
        print("2. Previous Month")
        print("3. Enter Specific Month/Year")
        print("4. Save Calendar to File")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            month += 1
            if month > 12:
                month = 1
                year += 1

        elif choice == '2':
            month -= 1
            if month < 1:
                month = 12
                year -= 1

        elif choice == '3':
            try:
                year = int(input("Enter year (e.g., 2025): "))
                month = int(input("Enter month (1-12): "))
                if month < 1 or month > 12:
                    raise ValueError
            except ValueError:
                print("❌ Invalid input. Press Enter to try again.")
                input()

        elif choice == '4':
            save_calendar_to_file(year, month)
            input("Press Enter to continue...")

        elif choice == '5':
            print("👋 Goodbye!")
            break

        else:
            input("❌ Invalid choice. Press Enter to continue...")

if __name__ == "__main__":
    main()
