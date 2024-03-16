def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2

operations = {
    '+' :  add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide
}

f_number  = float(input("What is the first number: "))
for symbol in operations:
   print(symbol)

should_continue = True
while should_continue:  
    operation_symbol = input("Pick up a operation: ")
    s_number  = float(input("What is the second number: "))
    calculation = operations[operation_symbol]
    answer = calculation(f_number, s_number)
    print(f"{f_number} {operation_symbol} {s_number}  = {answer}.")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
       f_number = answer
    else:
       should_continue = Falsen


    




# def output(operation,f_number,s_number):
#     if operation == "+":
#         return f"{f_number} {operation} {s_number}  = {add(f_number,s_number)}."
#     elif operation == "-":
#         return f"{f_number} {operation} {s_number}  = {subtract(f_number,s_number)}."
#     elif operation == "*":
#         return f"{f_number} {operation} {s_number}  = {multiply(f_number,s_number)}."
#     elif operation == "/":
#         return f"{f_number} {operation} {s_number}  = {divide(f_number,s_number)}."
#     else: 
#         return "Give me proper Operation from the above:"

# str = output(operation, f_number, s_number)
# print(str)