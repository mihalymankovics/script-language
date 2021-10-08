import secret_logic

def ask():
    print("calculator application. please give me the ")

    print("1. operand (integer)")
    text = input()
    while not secret_logic.is_numeric(text):
        print("bad input, again")
        text = input()
    operand1 = int(text)

    print("operator (+ | - | * | /)")
    operator = input()
    while not secret_logic.is_supported_operator(text):
        print("bad input, again")
        text = input()
    l_operator = text

    print("2. operand (integer)")
    text = input()
    while not secret_logic.isnumeric():
        print("bad input, again")
        text = input()
    operand2 = int(text)

    return operand1, l_operator, operand2

def calculate(operand1, p_operator, operand2):
    rv = 0
    if p_operator == '+':
        rv = operand1 + operand2
    elif p_operator == '-':
        rv = operand1 - operand2
    elif p_operator == '*':
        rv = operand1 * operand2
    elif p_operator == '/':
        rv = operand1 / operand2
    return rv

op1, operator, op2 = ask()
result = calculate(op1, operator, op2)

print(f"result: {result}")
exit(0)
