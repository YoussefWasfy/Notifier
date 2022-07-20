import datetime
import time as t


def get_d_t_from_user():
    date = input("Please enter a date (DD.MM.YYYY): ")
    time = input("Please enter the time (HH:MM): ")
    date = date + " " + time
    return date


# To ensure the user inputs an integer
def number_of_entries():
    input_bool = True
    while input_bool:
        try:
            no_inputs = int(input("How much data do you want to enter? "))
            input_bool = False
        except ValueError as e:
            print("Please enter a number")
            input_bool = True
    return no_inputs


def numbers_to_ordinals(n):
    return str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(4 if 10 <= n % 100 < 20 else n % 10, "th")


def calculate_and_display_dates():
    result = ""
    dt_objects = []
    reached_dates = []
    c = 0
    input_bool = True
    cond = True
    no_inputs = number_of_entries()
    # User entering date and time
    for i in range(no_inputs):
        while input_bool:
            date = get_d_t_from_user()
            # Avoiding wrong input from users
            try:
                date_and_time = datetime.datetime.strptime(date, "%d.%m.%Y %H:%M")
                input_bool = False
            except ValueError as e:
                print("Please enter date and time in the right format")
                input_bool = True
        dt_objects.append(date_and_time)

    while True:
        nearest_date = dt_objects[0]
        # Finding the nearest date
        for dt in dt_objects:
            if (dt - nearest_date).total_seconds() < 0:
                nearest_date = dt
        # Keep track of dates and  times reached
        date_time_now = datetime.datetime.now()
        difference = (nearest_date - date_time_now).total_seconds()
        # If the time has already passed no need to show it
        dt_objects.remove(nearest_date)
        if difference > 0:
            t.sleep(difference)
            c += 1
            if cond:
                result += f"The {numbers_to_ordinals(c)} date has been reached! {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}"
                cond = False
            else:
                result += f"\nThe {numbers_to_ordinals(c)} date has been reached! {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}"
        # If all the dates have been reached exit loop
        if len(dt_objects) == 0:
            print(result)
            return result
            break
