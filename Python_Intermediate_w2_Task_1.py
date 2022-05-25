class FormulaError(Exception):
    def __init__(self, message):
        super().__init__(message)


def calculator(sen):
    split_sen = sen.split()

    if len(split_sen) != 3:
        raise FormulaError("The expression must contains 3 elements")

    try:
        first_number = float(split_sen[0])
        second_number = float(split_sen[2])
    except ValueError:
        raise FormulaError("Not a number")

    if split_sen[1] not in ["+", "-", "*", "/"]:
        raise FormulaError("Not correct operator. Operator should be +, *, /, -")

    if split_sen[1] == "+":
        result = first_number + second_number
    elif split_sen[1] == "-":
        result = first_number - second_number
    elif split_sen[1] == "*":
        result = first_number * second_number
    elif split_sen[1] == "/":
        try:
            result = first_number / second_number
        except ZeroDivisionError:
            raise FormulaError("Zero division is prohibited")

    return result


print(calculator('1 / 8'))

