# Function definition

# def function_name(a, b, c);
#   <body of function>
#   return <return_value>

def add(a, b):
    total = a + b
    return total


add_a = add(1, 2)
add_b = add('hello', 'world')
add_c = add(1.0, 3)
# add_d = add(3, 'hello')

print(add_a, add_b, add_c)
