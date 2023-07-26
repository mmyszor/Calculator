def Calculate(number1, number2, operator):
    
    if operator == "+":
    
        result = number1+number2

    elif operator == '-':

        result = number1-number2

    elif operator == '*':

        result = number1*number2

    elif operator == '/':

        result = number1/number2

    elif operator == '^':

        result == number1**number2

    return result

number1 = float(input('Enter first nubmer:\n'))
operator = input('Choose calculation:\n+\n-\n*\n/\n^\n')
number2 = float(input('Enter second number:\n'))
result = Calculate(number1, number2, operator)
print(result)
