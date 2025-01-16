# Basic operations using lambda functions
"""In order to do the seven fundamental mathematical operations in Python (addition, subtraction, multiplication,
floating point division, integer division, the modulus operator, and the exponent), this program uses lambda functions
and an if-elif-else structure. The application asks the user to enter two variables and the action as a symbol
(for example, "+" for addition). The chosen operation is then carried out using a lambda function on the two variables,
and the outcome is returned. The application returns an error message if the user enters an incorrect symbol for the
    operation. The program offers an effective approach to carry out fundamental computations and is made to be
    straightforward and simple to use.
    """
def math_operation(op, x, y):
    
    if op == '+' or op == 'add':
        return lambda x, y: x + y
    elif op == '-' or op == 'subtract':
        return lambda x, y: x - y
    elif op == '*' or op == 'multiply':
        return lambda x, y: x * y
    elif op == '/' or op == 'divide':
        return lambda x, y: x / y
    elif op == '//' or op == 'integer divide':
        return lambda x, y: x // y
    elif op == '%' or op == 'modulus':
        return lambda x, y: x % y
    elif op == '**' or op == 'exponent':
        return lambda x, y: x ** y
    else:
        return None # Returns none if the operator symbol is not valid


def main():
    op = input("Enter the operation as a symbol (e.g. + for addition): ") # It asks the to enter the operator 
    x, y = input("Enter two values, separated by a space: ").split() # user should enter two values with space in between them
    x, y = float(x), float(y)
    function = math_operation(op, x, y)
    if function:
        result = function(x, y)
        print(f"{x} {op} {y} = {result}") # print the result
    else:
        print(f"{x} {op} {y} = Invalid operation") # If the operator is not recognized, it prints Invalid operation  


main()
