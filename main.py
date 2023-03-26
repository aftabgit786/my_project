import datetime
from my_project.utils.constant import MappingIndexF1
from my_project.utils.constant import MappingIndexF2
from my_project.utils.reader import get_file_contents


while True:
    input_file_name = input("Enter CSV file name or enter quit to exit: ")  # f1.csv or f2.csv

    if input_file_name == "quit":
        break

    if input_file_name == "f1.csv":
        while True:
            input_mode = input("Enter display mode (temperature/average) (enter 'back' to go back): ")
            if input_mode == "back":
                break

            if input_mode == "temperature":
                for file_content in get_file_contents(input_file_name):
                    date = file_content[MappingIndexF1.DATE]
                    max_temperature = float(file_content[MappingIndexF1.MAXIMUM_TEMPERATURE])
                    min_temperature = float(file_content[MappingIndexF1.MINIMUM_TEMPERATURE])

                    difference = max_temperature - min_temperature

                    print(
                        f"{date}, Maximum-Temp is {max_temperature} AND Minimum-Temp is {min_temperature} Differance, {difference}")

            elif input_mode == "average":
                for file_content in get_file_contents(input_file_name):
                    date = file_content[MappingIndexF1.DATE]
                    max_temperature = float(file_content[MappingIndexF1.MAXIMUM_TEMPERATURE])
                    min_temperature = float(file_content[MappingIndexF1.MINIMUM_TEMPERATURE])

                    average = (max_temperature - min_temperature) / 2

                    print(
                        f"{date}, Maximum-Temp is {max_temperature} AND Minimum-Temp is {min_temperature} of Average is: {average}")

            else:
                print("Invalid mode entered.")

    elif input_file_name == "f2.csv":
        while True:
            input_mode = input("Enter display mode (event/thunderstorm) (enter 'back' to go back): ")
            if input_mode == "back":
                break

            if input_mode == "event":
                for file_content in get_file_contents(input_file_name):
                    date = file_content[MappingIndexF2.DATE]
                    events = file_content[MappingIndexF2.EVENTS]

                    if events in ["Rain", "Snow", "Rain-Snow"]:
                        
                        print(f"{events} of the date {date}")

            elif input_mode == "thunderstorm":
                for file_content in get_file_contents(input_file_name):
                    date = file_content[MappingIndexF2.DATE]
                    events = file_content[MappingIndexF2.EVENTS]

                    if events == "Thunderstorm":
                        date_str = str(date)

                        date_to_names = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                        day_name = date_to_names.strftime("%A")

                        print(f"{date_str} of weather is Thunderstorm and day is {day_name}")

            else:
                print("Invalid mode entered.")

    else:
        print("Invalid file name entered.")
