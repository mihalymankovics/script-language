import sys

import secret_logic

print(f"{sys.argv}, {len(sys.argv)}")

def print_usage_and_exit():
    print("calcualtor app. usage: OPERAND OPERATOR OPERAND. f.e. 3 + 4")
    exit(-1)

def get_inputs():
    if len(sys.argv) != 4:
        print_usage_and_exit()

    if not secret_logic.is_numeric(sys.argv[1]):
        print_usage_and_exit()
    op1 = int(sys.argv[1])

    if not secret_logic.is_numeric(sys.argv[2]):
        print_usage_and_exit()
    operator = sys.argv[2]

    if not secret_logic.is_numeric(sys.argv[3]):
        print_usage_and_exit()
    op2 = int(sys.argv[3])
    return  op1, operator, op2

operand1, operator, operand2 = get_inputs()
result = secret_logic.calculate(op1, operator, op2)
print(f"result: {result}")
exit(0)