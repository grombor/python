any_number = 0

def handle_inputs(any_number):
    any_number = int(input("Type number: "))
    return any_number

def handle_operation(any_number):
    any_number = int(input(
        "Choose operation type: "
        "\n1. Addition"
        "\n2. Subtraction"
        "\n3. Multiplication"
        "\n4. Division"))
    if any_number not in range(1, 4):
        print("Bad answer. Should be in 1, 2, 3 or 4.")
    else: return any_number


def get_numbers():
    numbers_list = []
    try:
        numbers_list.append(handle_inputs(any_number))
        numbers_list.append(handle_inputs(any_number))
        numbers_list.append(handle_operation(any_number))
        return numbers_list
    except ValueError:
        print("ValueError: could not convert to integer")

def show_result(operand, num1, num2):
    if operand == 1: print("Result: " + str(num1 + num2))
    if operand == 2: print("Result: " + str(num1 - num2))
    if operand == 3: print("Result: " + str(num1 * num2))
    if operand == 4: print("Result: " + str(num1 / num2))