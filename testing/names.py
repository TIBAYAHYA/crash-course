from name_function import get_formatted_name

while True:
    print("Please enter your first name(or blank to quit): ")
    first_name = input()
    if first_name == "":
        break
    print("Please enter your last name(or blank to quit):")
    last_name = input()
    if last_name == "":
        break
    cool_name = get_formatted_name(first_name,last_name)

    print(f"Good to see you, {cool_name}")
        