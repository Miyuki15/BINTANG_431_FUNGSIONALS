def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "Pembagian nol tdk valid"
    else:
        return a / b


def tree(data):
    if type(data) in (int, float):
        return data
    elif type(data) is tuple and len(data) == 3:
        operator, left_operand, right_operand = data
        if operator == '+':
            return tree(left_operand) + tree(right_operand)
        elif operator == '-':
            return tree(left_operand) - tree(right_operand)
        elif operator == '*':
            return tree(left_operand) * tree(right_operand)
        elif operator == '/':
            return tree(left_operand) / tree(right_operand)


expression_tree = ('+', ('+', 389, 473), ('-', 73, 82))

result = tree(expression_tree)

print("hasilya = ", result)
