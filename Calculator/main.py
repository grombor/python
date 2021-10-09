from inputHandler import get_numbers, show_result

while True:
    try:
        my_list = get_numbers()
        show_result(my_list[2], my_list[0], my_list[1])
    except ValueError:
        print("Something went wrong. :(")
    exit_code = input("Finish work y / n ?")
    if exit_code.lower() == "y" : break
