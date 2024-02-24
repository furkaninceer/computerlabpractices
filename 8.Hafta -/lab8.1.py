global_variable = 27
global_counter=0

def a_function():
    global global_variable
    global_variable = global_variable + 1

def outer_function(outer_parameter = 123):
    outer_variable = global_variable + outer_parameter

    def inner_function(inner_parameter = 0):
        inner_variable = inner_parameter + outer_variable + global_variable
        return inner_variable

    result = inner_function(outer_variable)
    return result

def fibonacci(number):
    global global_counter
    global_counter+=1
    if number==1 or number==2:
        return 1
    else:
        previous=fibonacci(number-1)
        previous_2=fibonacci(number-2)
        #print(f"{number-1}. fibonacci number: {previous}")
        print(f"{number-2}. fibonacci number: {previous_2}")
        print(f"{number-1}. fibonacci number: {previous}")
        return previous+previous_2

result  = outer_function(7)
print(f'Result: {result}')

a_function()

result  = outer_function(7)
print(f'Result: {result}')

result  = outer_function()
print(f'Result: {result}')

print(f"7. fibonacci number: {fibonacci(4)}")
print(f'Global counter: {global_counter}')